# How the DeepSeek Harness Python SDK Works

## Summary

The Python SDK is a local client for the DeepSeek Harness runtime. A Python program does not implement the agent loop, execute tools, store sessions, or communicate with the model provider directly. It starts a separate `dsh` process and exchanges newline-delimited JSON-RPC messages with that process through standard input and standard output.

This report explains that design from the public Python API down to subprocess communication. It assumes no prior knowledge of DeepSeek Harness, web communication, or JSON-RPC. The explanation follows the implementation in `python/sdk/src/deepseek_harness/` and the executable example in `python/sdk/examples/minimal.py`, rather than the package README.

## Contents

- [The central idea](#the-central-idea)
- [The two Python API levels](#the-two-python-api-levels)
- [A complete run](#a-complete-run)
- [Configuration](#configuration)
- [Starting and initializing the runtime](#starting-and-initializing-the-runtime)
- [JSON-RPC from first principles](#json-rpc-from-first-principles)
- [How requests and responses are matched](#how-requests-and-responses-are-matched)
- [Sending a prompt](#sending-a-prompt)
- [Notifications, events, and completion](#notifications-events-and-completion)
- [Sessions and subagents](#sessions-and-subagents)
- [Understanding `RunResult`](#understanding-runresult)
- [Live notification handling](#live-notification-handling)
- [Runtime-to-Python requests](#runtime-to-python-requests)
- [Threads and synchronization](#threads-and-synchronization)
- [Shutdown and errors](#shutdown-and-errors)
- [Walking through `minimal.py`](#walking-through-minimalpy)
- [What the SDK does not do](#what-the-sdk-does-not-do)
- [Practical examples](#practical-examples)
- [Source map](#source-map)

## The central idea

The SDK consists of two programs that run at the same time:

```text
Your Python program
        |
        | JSON-RPC over local stdin/stdout
        v
The dsh runtime subprocess
        |
        | provider-specific network requests
        v
The configured model service
```

The first connection is local inter-process communication. The Python process writes text to the child process's standard input and reads text from its standard output. It is not a web connection, does not use HTTP, and does not open a network port.

The second connection is owned by the `dsh` runtime. Depending on its provider configuration, the runtime can use HTTP to contact DeepSeek or another model service. The Python SDK does not implement that provider protocol.

This separation lets Python remain a small control layer. The runtime owns agent behavior, plugins, tools, session state, and model communication.

## The two Python API levels

The package exposes a high-level API and a low-level transport API.

### `DeepSeekHarness`: the normal application API

Most programs should use `DeepSeekHarness`:

```python
from deepseek_harness import DeepSeekHarness

with DeepSeekHarness(
    provider="deepseek-official",
    model="deepseek-v4-flash",
    cwd="/path/to/workspace",
    dsh_home="/path/to/dsh-home",
) as harness:
    result = harness.run("Explain this project")

print(result.final_response)
```

This class manages runtime startup, initialization, session creation, prompt submission, event collection, final-text extraction, and shutdown.

### `HarnessClient`: the protocol API

`HarnessClient` manages the subprocess and JSON-RPC protocol. It supports direct method calls, raw notification subscriptions, runtime-to-Python requests, protocol responses, and diagnostics.

Use it when an application needs protocol-level control. It is not necessary for an ordinary agent turn.

## A complete run

The following sequence occurs when a program calls `harness.run("Explain this project")`:

```text
1. DeepSeekHarness starts the dsh subprocess if it is not already running.
2. Python sends an initialize request with workspace and model settings.
3. Python creates or accepts a session ID.
4. Python subscribes to notifications for that session and its descendants.
5. Python sends a session/prompt request containing text content blocks.
6. dsh returns a message ID, confirming that it accepted the request.
7. Python waits for an agent/inbox/spliced event containing that message ID.
8. dsh runs the agent and emits events and status notifications.
9. Python collects those messages until the root session becomes idle.
10. Python extracts the last assistant text and turn-ending reason.
11. harness.run returns a RunResult.
12. Leaving the with block asks dsh to shut down and reaps the process.
```

Steps 6 and 7 are distinct. A response to `session/prompt` means that the runtime accepted the command. The inbox event confirms that the particular user message entered the session that will process it.

## Configuration

`DeepSeekHarnessConfig` contains both agent settings and runtime-launch settings. Keyword arguments passed directly to `DeepSeekHarness` construct this configuration internally.

### Model settings

- `provider` selects a provider configured in the runtime. Its default is `deepseek-official`.
- `model` names the model. Its current default is `deepseek-v4-flash`.
- `reasoning_effort` optionally controls a supported model reasoning setting.
- `max_tokens` optionally limits model output.

These values are sent in the JSON-RPC `initialize` request. Python does not interpret them beyond constructing the request.

### Directory settings

- `cwd` is the workspace presented to the agent.
- `runtime_cwd` is the operating-system working directory used to launch the subprocess.

Both paths are resolved to absolute paths. If `runtime_cwd` is absent, it defaults to the resolved agent `cwd`. Keeping them separate allows the agent workspace and subprocess launch directory to differ.

### Runtime settings

- `dsh_bin` provides an explicit runtime executable.
- `profile` selects the `dsh` profile and defaults to `sdk`.
- `patches` adds repeated `--patch <absolute-path>` launch arguments.
- `dsh_home` supplies the runtime home and configuration directory.

When `dsh_bin` is absent, the client imports `deepseek_harness_runtime.resolve_bundled_launch_args()` and uses the bundled runtime package. A missing bundled package raises `FileNotFoundError`.

The SDK requires an explicit non-empty `dsh_home` or `DSH_HOME`. It never silently selects `~/.dsh`. An explicit `dsh_home` is resolved and written into the subprocess environment as `DSH_HOME`.

### Environment and credentials

The subprocess starts with a copy of the parent Python process's environment. Values from `env` overwrite entries in that copy. The convenience fields `base_url` and `api_key` then set `DEEPSEEK_BASE_URL` and `DEEPSEEK_API_KEY` in the child environment.

The API key is therefore not included in a JSON-RPC prompt or initialization payload. The runtime obtains it from its environment and owns subsequent provider communication.

### Timeouts

- `initialize_timeout_seconds` limits initialization and defaults to 30 seconds.
- `request_timeout_seconds` is the default for other request responses. `None` means no response deadline.
- `shutdown_timeout_seconds` bounds graceful shutdown phases and defaults to one second.

These timeouts concern protocol responses or shutdown. `Session.run()` itself waits for session notifications and has no separate turn-completion timeout in this implementation.

## Starting and initializing the runtime

`DeepSeekHarness.start()` is idempotent. It returns immediately after successful initialization when called again on the same instance.

On the first call, `HarnessClient.start()` builds arguments similar to:

```text
dsh --profile sdk --patch /absolute/optional-patch.yml
```

It then calls `subprocess.Popen` with piped stdin, stdout, and stderr, UTF-8 text mode, and line buffering. Two daemon threads start immediately:

- `dsh-runtime-reader` reads protocol messages from stdout.
- `dsh-runtime-stderr` retains the last 400 stderr lines for diagnostics.

After process startup, `DeepSeekHarness.start()` sends an `initialize` request. A typical request line is equivalent to:

```json
{"jsonrpc":"2.0","id":"generated-uuid","method":"initialize","params":{"cwd":"/absolute/workspace","provider":"deepseek-official","model":"deepseek-v4-flash"}}
```

Optional `reasoningEffort` and `maxTokens` fields appear only when configured. The result is validated with Pydantic as `InitializeResponse`, whose optional `serverInfo` has optional `name` and `version` fields.

If initialization fails, the client closes the subprocess before it propagates the exception. A JSON-RPC initialization error includes available stderr and exit diagnostics.

## JSON-RPC from first principles

JSON is a text format for values such as objects, lists, strings, numbers, booleans, and null. RPC means remote procedure call: one program asks another program to perform a named operation as though it were calling a function.

Here, "remote" means the separate local `dsh` process. It does not imply a machine across a network.

JSON-RPC 2.0 defines several message categories.

### Request

A request names a method, optionally supplies parameters, and includes an ID:

```json
{
  "jsonrpc": "2.0",
  "id": "abc",
  "method": "initialize",
  "params": {}
}
```

The sender expects exactly one response carrying the same ID.

### Successful response

```json
{
  "jsonrpc": "2.0",
  "id": "abc",
  "result": {}
}
```

### Error response

```json
{
  "jsonrpc": "2.0",
  "id": "abc",
  "error": {
    "code": 123,
    "message": "The operation failed",
    "data": {}
  }
}
```

The SDK converts this response into `JsonRpcError`, preserving its code, message, and optional data.

### Notification

A notification has a method but no ID:

```json
{
  "jsonrpc": "2.0",
  "method": "session.status",
  "params": {
    "sessionId": "session-123",
    "status": "idle"
  }
}
```

It reports asynchronous activity and does not receive a response. A single request can be followed by many notifications.

### Framing

The SDK writes each JSON object as one compact line followed by `\n`. The reader treats each stdout line as one complete message. This is often called JSON Lines or newline-delimited JSON framing.

Non-empty stdout lines that are not valid JSON are ignored. Runtime diagnostics belong on stderr so they do not interfere with the protocol stream.

## How requests and responses are matched

`HarnessClient._request_raw()` generates a UUID and creates a one-item `queue.Queue` for every outgoing request. It stores that queue in a dictionary keyed by request ID:

```text
_responses = {
    "initialize-id": queue_for_initialize,
    "prompt-id": queue_for_prompt,
}
```

The caller writes the request and blocks on its queue. Meanwhile, the reader thread parses stdout. When it receives a response, it removes the matching queue from `_responses` and places either the result or a `JsonRpcError` into that queue.

This design permits multiple outstanding requests because the response ID determines the correct waiting caller. A lock protects the shared response dictionary. A separate write lock ensures that two Python threads cannot interleave bytes while writing JSON lines to stdin.

`request()` wraps `_request_raw()`. It requires an object result and validates that object with the supplied Pydantic response model. For example, `session_prompt()` validates its result with a private model that requires a string `messageId`.

## Sending a prompt

`DeepSeekHarness.run()` creates a `Session`, then calls `Session.run()`.

A string input is converted into the runtime's content-block representation:

```python
"Explain this project"
```

becomes:

```python
[
    {
        "type": "text",
        "text": "Explain this project",
    }
]
```

Callers can also pass a list of JSON objects directly. The SDK does not normalize or validate that list further before sending it.

`HarnessClient.session_prompt()` sends a request equivalent to:

```json
{
  "jsonrpc": "2.0",
  "id": "prompt-request-id",
  "method": "session/prompt",
  "params": {
    "sessionId": "session-123",
    "contentBlocks": [
      {"type": "text", "text": "Explain this project"}
    ]
  }
}
```

The direct response contains a `messageId`. `Session.run()` then waits for a `session.event` notification whose event type is `agent/inbox/spliced` and whose `data.inserted` list contains that message ID.

Notifications that arrive before this receipt but do not match it are skipped by the high-level run collector. After the receipt, notifications are collected until completion.

## Notifications, events, and completion

The reader classifies an incoming message without an ID but with a method as a notification. It converts the message into:

```python
Notification(method=method_name, payload=params_object)
```

A `session.event` notification contains an event inside its payload:

```json
{
  "jsonrpc": "2.0",
  "method": "session.event",
  "params": {
    "sessionId": "session-123",
    "event": {
      "type": "assistant/message",
      "data": {
        "content": [
          {"type": "text", "text": "Here is the answer."}
        ]
      }
    }
  }
}
```

During a high-level run, every accepted notification is appended to `RunResult.notifications`. When the notification is a `session.event` for the root session, its nested event object is also appended to `RunResult.events`.

The completion condition is a root-session status notification with `status` equal to `idle`:

```json
{
  "method": "session.status",
  "params": {
    "sessionId": "session-123",
    "status": "idle"
  }
}
```

The SDK does not infer completion from an assistant message or from a quiet period. It continues blocking until it observes this explicit status.

## Sessions and subagents

`DeepSeekHarness.start_session()` accepts an optional session ID. Without one, it creates a value of the form `session-<uuid>`.

A `Session` is a small object holding the harness and session ID. It does not own another subprocess. Multiple `Session` objects created by one harness share the initialized runtime.

The client can follow descendant sessions created by subagents. When it sees a `subagent.started` notification with `parentSessionId` and `childSessionId`, it records the parent relationship. A session subscription then accepts notifications for the requested root and descendants discovered through those relationships.

The ancestry check tracks visited IDs to avoid looping forever if malformed relationships contain a cycle.

The high-level event collector is narrower than the notification subscription: it retains all matching notifications, but it adds an event to `RunResult.events` only when the notification's `sessionId` exactly equals the root `Session.id`. Descendant activity remains visible through `RunResult.notifications`.

## Understanding `RunResult`

`Session.run()` returns:

```python
RunResult(
    session_id=...,
    final_response=...,
    finish_reason=...,
    events=...,
    notifications=...,
)
```

### `session_id`

This is the root session ID used for the prompt.

### `events`

This is the list of root-session event dictionaries collected after the prompt receipt and before the root session became idle. Event values remain generic JSON rather than one Python class per event type.

### `notifications`

This list preserves the method and payload of every collected root-or-descendant notification. It can include `session.event`, `session.status`, `subagent.started`, and `subagent.finished` messages.

### `final_response`

The helper searches backward through `events` for the latest `assistant/message`. It supports content stored either at `event.data.message.content` or directly at `event.data.content`. It concatenates the `text` value of every content block whose type is `text`.

Structured blocks such as tool use are not represented in this convenience string. They remain available in the raw events.

If no usable assistant message exists, `final_response` is an empty string.

### `finish_reason`

The helper searches backward for the latest `turn/end` event and returns `event.data.reason.kind`. It returns `None` if no `turn/end` event exists. If such an event exists without a string reason kind, it raises `SdkProtocolError` because the runtime message violates the SDK's expectation.

## Live notification handling

The high-level API is synchronous: `run()` does not return until the session becomes idle. It can still expose activity while it waits:

```python
from deepseek_harness import DeepSeekHarness, Notification


def observe(notification: Notification) -> None:
    print(notification.method, notification.payload)


with DeepSeekHarness(...) as harness:
    result = harness.run(
        "Inspect the project",
        on_notification=observe,
    )
```

The background reader thread receives notifications. The thread executing `run()` removes them from the subscription queue and invokes the callback. The callback is therefore part of the synchronous waiting path, not arbitrary work running on the reader thread.

A slow or failing callback delays or interrupts the request that is draining it. Applications should keep the callback bounded and move expensive processing elsewhere.

The lower-level client also provides `subscribe_notifications()`, `subscribe_session_notifications()`, `NotificationSubscription.next()`, and `NotificationSubscription.drain()` for direct queue control.

## Runtime-to-Python requests

JSON-RPC is bidirectional. A runtime message containing both an ID and a method is classified as a request from the runtime to Python:

```json
{
  "jsonrpc": "2.0",
  "id": "runtime-request-id",
  "method": "some/method",
  "params": {}
}
```

The client exposes it through `next_request()` as an `IncomingRequest`. Application code can reply with:

```python
client.respond(request.id, result)
```

or:

```python
client.respond_error(
    request.id,
    code=123,
    message="Unable to handle request",
    data=None,
)
```

This facility differs from notifications because the runtime request has an ID and expects a response. The normal `DeepSeekHarness.run()` path does not automatically consume or answer these requests.

## Threads and synchronization

The SDK presents a synchronous API but uses background threads for process I/O.

```text
Application thread
  writes requests
  waits on per-request queues
  consumes subscription queues
  invokes notification callbacks

Reader thread
  reads stdout lines
  parses JSON
  routes responses, notifications, and incoming requests

Stderr thread
  reads stderr lines
  retains the latest 400 lines
```

`self._lock` protects shared dictionaries and session relationships. `self._write_lock` serializes writes to subprocess stdin. Thread-safe queues transfer messages and exceptions between the reader and application threads.

If stdout closes or the reader fails, `_fail_waiters()` distributes an exception to every pending response queue, notification subscription, the general notification queue, and the incoming-request queue. Blocked callers therefore wake instead of waiting indefinitely for a process that has exited.

## Shutdown and errors

### Shutdown

`DeepSeekHarness.close()` delegates to `HarnessClient.close()` and clears its initialized flag. The client:

1. sends a `shutdown` request and gives it a bounded opportunity to finish;
2. closes subprocess stdin;
3. waits briefly after a successful shutdown response;
4. sends terminate if the process remains alive;
5. sends kill if termination does not complete in time;
6. fails remaining waiters;
7. briefly joins the reader threads.

The context-manager form ensures that this cleanup runs even when code inside the `with` block raises an exception.

### `JsonRpcError`

The transport worked, but the runtime returned an error object. The exception exposes `code`, `message`, and `data`.

### `TransportClosedError`

The runtime is not running, writing failed, stdout closed, or the subprocess exited. When possible, the message includes the process exit code and captured stderr tail.

### `TimeoutError`

A request did not receive a response before its configured deadline. Request timeout accounting uses `time.monotonic()`, which is not affected by changes to the system wall clock.

Initialization timeouts also report the selected profile. Request timeouts include runtime diagnostics when available.

### `SdkProtocolError`

The runtime returned data that could be parsed as JSON but violated a high-level SDK expectation. The current final-result path uses this error for a malformed `turn/end` reason.

### Pydantic validation errors and `TypeError`

Typed responses are validated with Pydantic. A result that is not a JSON object raises `TypeError`; an object missing required response fields raises a Pydantic validation error.

## Walking through `minimal.py`

The example accepts a prompt and these options:

```text
--workspace
--dsh-home
--profile
--session-id
--provider
--model
--max-tokens
```

It reads `DSH_HOME` as the default for `--dsh-home` and rejects execution when neither provides a non-empty path. The model defaults from `DSH_MODEL`, falling back to `deepseek-v4-flash`.

The essential code is:

```python
with DeepSeekHarness(
    provider=args.provider,
    model=args.model,
    max_tokens=args.max_tokens,
    cwd=str(workspace),
    dsh_home=str(dsh_home),
    profile=args.profile,
) as harness:
    result = harness.run(args.prompt, session_id=args.session_id)

print(result.final_response)
```

Entering the context starts and initializes the subprocess. `run()` submits one prompt and waits for the session to become idle. Exiting the context shuts down the subprocess. The example prints only the convenience text, not raw events, tool activity, or notifications.

## What the SDK does not do

The Python package does not itself:

- implement the agent loop;
- call a model provider directly;
- execute shell, browser, or computer tools;
- parse provider-specific streaming formats;
- store durable sessions;
- define a Python class for every runtime event;
- expose an asynchronous `asyncio` API;
- communicate with `dsh` through HTTP.

Its responsibility is smaller:

```text
launch the runtime
+ send JSON-RPC commands
+ route responses
+ collect asynchronous notifications
+ return a convenient synchronous result
```

## Practical examples

### Reuse one runtime for multiple independent sessions

```python
from deepseek_harness import DeepSeekHarness

with DeepSeekHarness(...) as harness:
    first = harness.run("Summarize package A")
    second = harness.run("Summarize package B")

print(first.session_id, first.final_response)
print(second.session_id, second.final_response)
```

The harness starts one subprocess. Each call without an explicit ID creates a new session ID.

### Reuse a session explicitly

```python
with DeepSeekHarness(...) as harness:
    session = harness.start_session("my-session")
    first = session.run("Inspect the repository")
    second = session.run("Now focus on the Python SDK")
```

Both prompts use the same session identifier and the same runtime process. Whether and how prior context is restored or retained is a runtime and profile concern, not logic implemented by the `Session` Python class.

### Inspect structured results

```python
with DeepSeekHarness(...) as harness:
    result = harness.run("Perform the task")

print("finish reason:", result.finish_reason)

for event in result.events:
    print("event:", event.get("type"), event)

for notification in result.notifications:
    print("notification:", notification.method, notification.payload)
```

Use `final_response` for a simple text answer. Use `events` and `notifications` when the application needs lifecycle, tool, or subagent information.

## Source map

- `python/sdk/src/deepseek_harness/api.py` defines `DeepSeekHarnessConfig`, `DeepSeekHarness`, `Session`, `RunResult`, prompt normalization, final-text extraction, and finish-reason extraction.
- `python/sdk/src/deepseek_harness/client.py` defines subprocess startup, JSON-RPC requests, reader threads, notification subscriptions, session-tree filtering, shutdown, and diagnostics.
- `python/sdk/src/deepseek_harness/models.py` defines recursive JSON types, `Notification`, `IncomingRequest`, and initialization response models.
- `python/sdk/src/deepseek_harness/errors.py` defines transport, protocol, and JSON-RPC exception types.
- `python/sdk/src/deepseek_harness/__init__.py` defines the package's public imports.
- `python/sdk/examples/minimal.py` demonstrates one prompt through the high-level synchronous API.
