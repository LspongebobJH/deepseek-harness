<!-- Source: https://deepwiki.com/deepseek-ai/deepseek-harness/2-core-architecture; extracted 2026-09-24 -->

# Core Architecture

Relevant source files

- [docs/architecture.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.i18n.yaml)
- [docs/architecture.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1)
- [docs/architecture.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.zh.md?plain=1)
- [docs/subsystems/core.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/subsystems/core.i18n.yaml)
- [docs/subsystems/core.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/subsystems/core.md?plain=1)
- [docs/subsystems/core.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/subsystems/core.zh.md?plain=1)
- [packages/core/agent-loop/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/README.i18n.yaml)
- [packages/core/agent-loop/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/README.md?plain=1)
- [packages/core/agent-loop/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/README.zh.md?plain=1)
- [packages/core/agent-loop/src/agent.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts)
- [packages/core/agent-loop/tests/tool-order.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/tests/tool-order.spec.ts)
- [packages/core/agent/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/README.i18n.yaml)
- [packages/core/agent/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/README.md?plain=1)
- [packages/core/agent/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/README.zh.md?plain=1)
- [packages/core/agent/src/types.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/src/types.ts)
- [packages/core/system-prompt/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/README.i18n.yaml)
- [packages/core/system-prompt/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/README.md?plain=1)
- [packages/core/system-prompt/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/README.zh.md?plain=1)
- [packages/core/system-prompt/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/src/index.ts)
- [packages/core/system-prompt/tests/scoped.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/tests/scoped.spec.ts)
- [packages/core/system-prompt/tests/system-prompt.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/tests/system-prompt.spec.ts)
- [packages/core/system-prompt/tests/tool-order.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/system-prompt/tests/tool-order.spec.ts)
- [packages/core/tools/tests/scoped.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/tools/tests/scoped.spec.ts)

This page provides an overview of the core architectural foundations of DeepSeek Harness (`dsh`), powered by the **Cordis** plugin framework [docs/architecture.md9-11](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L9-L11) Every functional subsystem—ranging from model adapters and tool registries to session logging and the core agent loop—is implemented as a modular plugin contributing services, typed events, and reversible effects to a shared context [docs/architecture.md9-11](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L9-L11)

For deep technical details on each subsystem, refer to the child pages:

- [Cordis Framework & Vendored Dependencies](./2.1-cordis-framework-and-vendored-dependencies.md)
- [Plugin Composition: Profiles, Bundles & Configuration](./2.2-plugin-composition:-profiles-bundles-and-configuration.md)
- [Event Bus & Capability Seams](./2.3-event-bus-and-capability-seams.md)

---

## 2.1 Cordis Framework & Vendored Dependencies

The system relies on a vendored version of the **Cordis** framework to manage plugin lifecycles, service injection, and dependency resolution [docs/architecture.md9-11](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L9-L11) Plugins declare dependencies via `inject` annotations and merge their TypeScript service declarations directly into the global `Context` type [packages/core/agent/src/types.ts17-26](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/src/types.ts#L17-L26)

When a plugin unloads, Cordis automatically unwinds all associated registrations, ensuring clean fiber disposal and zero state leakage across execution boundaries [docs/architecture.md11-13](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L11-L13) For deep dives into lifecycle hooks, Context declaration merging, and local framework modifications, see [Cordis Framework & Vendored Dependencies](./2.1-cordis-framework-and-vendored-dependencies.md).

Sources: [docs/architecture.md9-14](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L9-L14) [packages/core/agent/src/types.ts17-26](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent/src/types.ts#L17-L26)

---

## 2.2 Plugin Composition: Profiles, Bundles & Configuration

A running `dsh` instance is dynamically assembled at boot time from ordered patch layers [docs/architecture.md17](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L17-L17) The composition model uses three primary layers:

- **Profiles:** Named configuration compositions (such as `web`, `headless`, `sdk`, `sdk-minimal`, and `acp`) that stack bundles and user overlay paths [docs/architecture.md19-20](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L19-L20)
- **Bundles:** Distribution packages (such as [`dsh-base`](../packages/bundle/base/README.md) [docs/architecture.md25](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L25-L25)) that bundle baseline Cordis configuration rows and their corresponding modules [docs/architecture.md21-22](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L21-L22)
- **Patches:** YAML override files (`cordis.patch.yml`) targeting configuration rows by ID to customize behavior [docs/architecture.md27-28](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L27-L28)

Running `dsh --profile web --dump-config` prints the resolved configuration tree [docs/architecture.md33-37](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L33-L37) For complete assembly mechanics and configuration schemas, see [Plugin Composition: Profiles, Bundles & Configuration](./2.2-plugin-composition:-profiles-bundles-and-configuration.md).

Sources: [docs/architecture.md15-42](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L15-L42)

---

## 2.3 Event Bus & Capability Seams

Subsystems communicate via a centralized typed event bus and swappable interface boundaries known as **capability seams** [docs/architecture.md74-79](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L74-L79) Communication is structured across distinct channels:

1. **Session Events:** Durable facts broadcast through `session/event` and appended to the session log for persistence and historical replay [docs/architecture.md76](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L76-L76)
2. **Agent Events:** Live lifecycle hooks (`agent/*` events such as `agent/pre-step` and `agent/request`) governing agent execution and tool interception [docs/architecture.md77-78](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L77-L78)
3. **Capability Seams:** Abstracted runtime adapters (such as `ctx.llm`, `ctx.tools`, and `ctx.fs`) allowing underlying implementations to be swapped transparently [docs/architecture.md79-80](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L79-L80)

For a complete breakdown of event producers, consumers, and waterfall execution rules, see [Event Bus & Capability Seams](./2.3-event-bus-and-capability-seams.md).

Sources: [docs/architecture.md74-80](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L74-L80)

---

## Subsystem Architecture & Code Mapping

The following diagram bridges natural language concepts to concrete code entities and service keys within the repository.

**Core Architecture Component Map**

Sources: [docs/architecture.md59-71](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L59-L71) [packages/core/agent-loop/src/agent.ts72-112](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts#L72-L112)

---

## Turn Flow and Execution Pipeline

The agent loop coordinates turns and step boundaries, driving state transitions through asynchronous waterfalls and event dispatches.

**Step Execution Pipeline**

Sources: [packages/core/agent-loop/src/agent.ts128-148](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/core/agent-loop/src/agent.ts#L128-L148) [docs/architecture.md86-118](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/architecture.md?plain=1#L86-L118)

---

## Subsystem Navigation

- [Cordis Framework & Vendored Dependencies](./2.1-cordis-framework-and-vendored-dependencies.md) — Deep dive into plugin lifecycles, service injection, and Context merging.
- [Plugin Composition: Profiles, Bundles & Configuration](./2.2-plugin-composition:-profiles-bundles-and-configuration.md) — Assembly of running instances via profiles, bundles, and configuration catalogs.
- [Event Bus & Capability Seams](./2.3-event-bus-and-capability-seams.md) — Detailed event distribution model and capability seam patterns.
