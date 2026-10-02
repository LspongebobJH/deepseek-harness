<!-- Source: https://deepwiki.com/deepseek-ai/deepseek-harness/3-agent-system; extracted 2026-09-24 -->

# Agent System

Relevant source files

- [docs/architecture.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.i18n.yaml)
- [docs/architecture.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1)
- [docs/architecture.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.zh.md?plain=1)
- [packages/core/agent-loop/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/README.i18n.yaml)
- [packages/core/agent-loop/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/README.md?plain=1)
- [packages/core/agent-loop/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/README.zh.md?plain=1)
- [packages/core/agent-loop/src/agent.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts)
- [packages/core/agent-loop/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/index.ts)
- [packages/core/agent-loop/tests/agent.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/agent.spec.ts)
- [packages/core/agent-loop/tests/cancel.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/cancel.spec.ts)
- [packages/core/agent-loop/tests/config-session-id.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/config-session-id.spec.ts)
- [packages/core/agent-loop/tests/contract-regressions.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/contract-regressions.spec.ts)
- [packages/core/agent-loop/tests/coverage-edges.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/coverage-edges.spec.ts)
- [packages/core/agent-loop/tests/interception.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/interception.spec.ts)
- [packages/core/agent-loop/tests/loop.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/loop.spec.ts)
- [packages/core/agent-loop/tests/resume.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/resume.spec.ts)
- [packages/core/agent-loop/tests/scope-lifecycle.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/scope-lifecycle.spec.ts)
- [packages/core/agent-loop/tests/tool-order.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/tool-order.spec.ts)
- [packages/core/agent/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/README.i18n.yaml)
- [packages/core/agent/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/README.md?plain=1)
- [packages/core/agent/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/README.zh.md?plain=1)
- [packages/core/agent/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/src/index.ts)
- [packages/core/agent/src/types.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/src/types.ts)
- [packages/core/agent/tests/agent.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/tests/agent.spec.ts)
- [packages/core/scope/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/scope/README.i18n.yaml)
- [packages/core/scope/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/scope/README.md?plain=1)
- [packages/core/scope/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/scope/README.zh.md?plain=1)
- [packages/core/scope/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/scope/src/index.ts)
- [packages/core/scope/src/store.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/scope/src/store.ts)
- [packages/core/scope/tests/scope.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/scope/tests/scope.spec.ts)
- [packages/core/scope/tests/store.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/scope/tests/store.spec.ts)
- [packages/core/system-prompt/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/README.i18n.yaml)
- [packages/core/system-prompt/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/README.md?plain=1)
- [packages/core/system-prompt/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/README.zh.md?plain=1)
- [packages/core/system-prompt/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/src/index.ts)
- [packages/core/system-prompt/tests/scoped.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/tests/scoped.spec.ts)
- [packages/core/system-prompt/tests/system-prompt.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/tests/system-prompt.spec.ts)
- [packages/core/system-prompt/tests/tool-order.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/tests/tool-order.spec.ts)
- [packages/core/tools/tests/scoped.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/tools/tests/scoped.spec.ts)

The Agent System serves as the core orchestration layer of DeepSeek Harness (`dsh`). It manages the creation, driving, lifecycle, and tool execution of autonomous agents within a modular, plugin-based architecture powered by the **Cordis** framework [docs/architecture.md10-12](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L10-L12)

For detailed technical dives, see the child pages:

- [Agent Loop & Lifecycle](./3.1-agent-loop-and-lifecycle.md)
- [Tool Registry & Execution Pipeline](./3.2-tool-registry-and-execution-pipeline.md)
- [Session Log & Persistence](./3.3-session-log-and-persistence.md)
- [Subagent Orchestration](./3.4-subagent-orchestration.md)
- [LLM Adapters & Streaming](./3.5-llm-adapters-and-streaming.md)

---

## Core Components & Entity Mapping

Agents are structured around a turn-based state machine where a **Turn** encapsulates zero or more **Steps**, and a step represents an LLM request combined with tool executions [docs/architecture.md75-82](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L75-L82) The agent ecosystem relies on several core packages and service keys.

| Service | Context Key | Responsibility |
| --- | --- | --- |
| `AgentRegistry` | `ctx.agents` | Tracks live agents, provides handles, and carries the process-local initiator scope [packages/core/agent/README.md11-12](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/README.md?plain=1#L11-L12) |
| `AgentLoop` | `ctx.agentLoop` | The concrete driver implementation managing loop instantiations and factories [packages/core/agent-loop/README.md12-13](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/README.md?plain=1#L12-L13) |
| `ReactLoopAgent` | N/A | The default internal driver implementing the public `Agent` interface [packages/core/agent-loop/src/agent.ts70](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts#L70-L70) |

Agent System Entity Map

Sources: [packages/core/agent-loop/src/agent.ts70-109](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts#L70-L109) [packages/core/agent/src/types.ts12-15](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/src/types.ts#L12-L15) [packages/core/agent/README.md11-12](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/README.md?plain=1#L11-L12)

---

## 3.1 Agent Loop & Lifecycle

The default agent loop driver (`dsh-agent-loop`) manages agent instantiation, session binding, and turn-by-turn execution. It processes durable inbox events, coordinates cancellation, and maintains epoch headers.

For deep dives into turn/step state machines, inbox management, epoch headers, and publication transactions, see [Agent Loop & Lifecycle](./3.1-agent-loop-and-lifecycle.md).

Sources: [docs/architecture.md75-93](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L75-L93) [packages/core/agent-loop/src/agent.ts70-126](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts#L70-L126) [packages/core/agent-loop/README.md12-13](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/README.md?plain=1#L12-L13)

---

## 3.2 Tool Registry & Execution Pipeline

Tools are registered globally or scoped to individual agents via `ctx.tools`. The `ToolRuntime` service executes tool calls through a guarded execution waterfall consisting of `tools/pre-execute`, `tools/execute`, and `tools/post-execute` stages, supporting parallel execution limits and Code Mode generation.

For details on tool registration, waterfall interceptors, and scheduling, see [Tool Registry & Execution Pipeline](./3.2-tool-registry-and-execution-pipeline.md).

Sources: [docs/architecture.md57](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L57-L57) [docs/architecture.md90](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L90-L90)

---

## 3.3 Session Log & Persistence

All agent actions, messages, and tool outcomes are recorded in an append-only `SessionEvent` log managed by `ctx.sessions`. The model's conversation history is dynamically projected from this log using `deriveMessages()`, allowing deterministic forking and persistence across JSONL and SQLite backends.

For information on projection rules, event schemas, and lineage tracking, see [Session Log & Persistence](./3.3-session-log-and-persistence.md).

Sources: [docs/architecture.md68-71](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L68-L71) [docs/architecture.md89](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L89-L89)

---

## 3.4 Subagent Orchestration

Parent agents can spawn and delegate workloads to subagents via the `ctx.agents` service. Subagents support both one-shot and continuable execution modes across in-process or out-of-process drivers (such as ACP, Codex, Claude Code, and the DSH SDK).

For orchestration policies, policy inheritance, and reporting conventions, see [Subagent Orchestration](./3.4-subagent-orchestration.md).

Sources: [packages/core/agent/README.md28-33](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/README.md?plain=1#L28-L33)

---

## 3.5 LLM Adapters & Streaming

The agent loop decouples model communication through the `LlmRuntime` seam (`ctx.llm`). Adapters normalize streaming responses, handle retries, track token metering, and bridge provider-specific requirements.

For details on streaming protocols, block assembly, and adapter implementations, see [LLM Adapters & Streaming](./3.5-llm-adapters-and-streaming.md).

Sources: [docs/architecture.md61](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L61-L61) [packages/core/agent-loop/src/agent.ts19-27](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts#L19-L27)

---

## Service Interactions Overview

The following sequence diagram illustrates how `ReactLoopAgent` orchestrates prompts, sessions, LLM streaming, and tool execution during a single agent step.

Agent Step Orchestration

Sources: [docs/architecture.md75-93](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L75-L93) [packages/core/agent-loop/src/agent.ts18-37](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts#L18-L37) [packages/core/agent-loop/src/tool-calls.ts36](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/tool-calls.ts#L36-L36) [packages/core/agent-loop/src/agent.ts37](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts#L37-L37)
