# How `@deepseek-ai/dsh-browser-use` Works

This package is a Cordis capability registry for browser backends. It does not
launch Chromium, define browser actions, expose model tools, or select a backend
at runtime. Its job is to make one provider reservation visible as
`ctx.browserUse` and to reject competing providers.

## 1. How the package is defined

The package is an ESM workspace package whose entry point is
[`src/index.ts`](../packages/browser-use/browser-use/src/index.ts). Its default
export is `BrowserUseRegistry`, a class extending Cordis `Service`:

```ts
export default BrowserUseRegistry
```

The constructor calls `super(ctx, 'browserUse')`. Cordis therefore installs one
service instance on a context and exposes it as `ctx.browserUse`. TypeScript
declaration merging adds that property to Cordis's `Context` interface:

```ts
declare module '@deepseek-ai/cordis' {
  interface Context {
    browserUse: BrowserUseRegistry
  }
}
```

The service stores exactly one private value, `registration`, containing a
branded `BrowserUseProviderName`. The brand is defined in
[`src/brand.ts`](../packages/browser-use/browser-use/src/brand.ts); it is a
compile-time identity marker, not a runtime validator.

The public API is intentionally small:

- `providerName` reads the currently reserved provider name.
- `register(name)` reserves the only slot and returns an asynchronous disposer.

`register` throws if the slot is already occupied, even when the new name is
the same. The error includes the existing provider name, which makes profile
misconfiguration visible.

## 2. How it is registered in Cordis

A composition mounts the registry as a normal Cordis plugin:

```yaml
- name: '@deepseek-ai/dsh-browser-use'
```

Equivalent code is `await ctx.plugin(BrowserUseRegistry)`. Mounting creates the
service but does not reserve a provider; `ctx.browserUse.providerName` is
initially `undefined`.

The registry itself uses Cordis effects for the contribution. The important
operation is:

```ts
return this.ctx.effect(() => {
  this.registration = name
  return () => { this.registration = undefined }
}, 'browserUse.register()')
```

This means registration is tied to Cordis ownership. The returned function is
the disposer for that exact effect, rather than a general “clear” operation.
Cordis can also run it automatically when the contributing plugin unloads.

## 3. How other packages and the agent loop use it

Provider packages depend on `@deepseek-ai/dsh-browser-use` and declare
`browserUse` in their injection list. For example, the Playwright MCP provider
declares:

```ts
export const inject = ['browserUse', 'agents', 'tools', 'systemPrompt']
```

Its `apply` function validates configuration and calls the shared runtime
helper with the provider name `playwright-mcp`. The Stagehand provider follows
the same pattern and registers `stagehand-native`.

The runtime helper performs the provider registration before creating its
Session resource manager:

```ts
yield ctx.browserUse.register(BrowserUseProviderName(options.name))
```

After that reservation, the provider owns the browser-specific behavior:

1. It creates one browser/MCP resource per live Agent or Session according to
   its own launch or attachment configuration.
2. It listens to `agent/created` so client startup and tool discovery complete
   before the Agent begins handling queued input.
3. It adds provider-owned schemas and handlers to the normal DSH tool
   pipeline. `tools/execute` checks the owning Agent/Session and serializes
   calls through the provider's resource manager.
4. It contributes provider instructions to `system-prompt/assemble` when the
   current Agent owns a ready browser resource.

The agent loop remains DSH's responsibility. The shared registry does not add
an agent-loop branch, common browser method, model request, or Session event.
Provider tools and returned results use the ordinary tool execution and Session
logging paths. This is why different backends can expose different tool names,
schemas, result formats, and cleanup behavior without changing the registry.

The registry can also be consumed directly by another plugin that only needs
to inspect availability:

```ts
inject: ['browserUse']
// ctx.browserUse.providerName
```

In practice, provider implementations use the name for diagnostics and
ownership checks; consumers should not treat it as a selector that can switch
providers.

## 4. How it deregisters

Deregistration happens through the disposer returned by `register`, or through
the contributing plugin's disposal. Calling it clears `registration`, after
which another provider may reserve the slot:

```ts
const dispose = ctx.browserUse.register(name)
await dispose()
ctx.browserUse.register(otherName)
```

The disposer is idempotent in the Cordis effect system and is tied to its own
registration. A stale disposer cannot clear a later registration. The package
tests explicitly cover this sequence and plugin unload:
[`tests/registry.spec.ts`](../packages/browser-use/browser-use/tests/registry.spec.ts).

Provider cleanup must happen before releasing the reservation. Providers stop
admitting new tool calls, wait for active calls and owned resources to settle,
close launched browsers or disconnect from attached browsers, and only then
allow the registration effect to dispose. The registry does not perform any of
that work because it does not own browser resources.

## End-to-end lifecycle

```text
profile/Cordis composition
        |
        v
mount BrowserUseRegistry -> ctx.browserUse (empty)
        |
        v
provider apply() -> register(branded name)
        |
        v
provider installs tools/resources and participates in Agent creation
        |
        v
provider teardown -> stop calls, clean resources
        |
        v
effect disposer -> providerName becomes undefined
```

The architectural rule is simple: the package owns exclusivity and lifecycle
of the registration effect; each provider owns browser operations and Session
resources; DSH owns the task loop and the normal tool/logging pipeline.

## Related source

- [Browser-use subsystem](../docs/subsystems/browser-use.md)
- [Package README](../packages/browser-use/browser-use/README.md)
- [MCP runtime integration](../packages/experimental/browser-use-runtime/src/mcp.ts)
- [Stagehand provider](../packages/experimental/browser-use-stagehand-native/src/index.ts)
- [Provider-registration decision](../.agents/notes/implemented/architecture/2026-09-12-browser-use-provider-registration.md)
