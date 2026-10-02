<!-- Source: https://deepwiki.com/deepseek-ai/deepseek-harness/5-api-layer-and-host-client-bridge; extracted 2026-09-24 -->

# API Layer & Host-Client Bridge

Relevant source files

- [.agents/notes/implemented/architecture/2026-07-28-api-browser-trust-boundary.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/.agents/notes/implemented/architecture/2026-07-28-api-browser-trust-boundary.i18n.yaml)
- [.agents/notes/implemented/architecture/2026-07-28-api-browser-trust-boundary.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/.agents/notes/implemented/architecture/2026-07-28-api-browser-trust-boundary.md?plain=1)
- [.agents/notes/implemented/architecture/2026-07-28-api-browser-trust-boundary.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/.agents/notes/implemented/architecture/2026-07-28-api-browser-trust-boundary.zh.md?plain=1)
- [.agents/notes/implemented/architecture/2026-08-02-typert-remote-method-calls.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/.agents/notes/implemented/architecture/2026-08-02-typert-remote-method-calls.i18n.yaml)
- [.agents/notes/implemented/architecture/2026-08-02-typert-remote-method-calls.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/.agents/notes/implemented/architecture/2026-08-02-typert-remote-method-calls.md?plain=1)
- [.agents/notes/implemented/architecture/2026-08-02-typert-remote-method-calls.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/.agents/notes/implemented/architecture/2026-08-02-typert-remote-method-calls.zh.md?plain=1)
- [docs/api-gateway.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/api-gateway.i18n.yaml)
- [docs/api-gateway.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/api-gateway.md?plain=1)
- [docs/api-gateway.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/api-gateway.zh.md?plain=1)
- [packages/api/gateway/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/README.i18n.yaml)
- [packages/api/gateway/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/README.md?plain=1)
- [packages/api/gateway/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/README.zh.md?plain=1)
- [packages/api/gateway/src/client/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/src/client/index.ts)
- [packages/api/gateway/tests/gateway.client.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/tests/gateway.client.spec.ts)
- [packages/api/remotes/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/remotes/README.i18n.yaml)
- [packages/api/remotes/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/remotes/README.md?plain=1)
- [packages/api/remotes/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/remotes/README.zh.md?plain=1)
- [packages/api/remotes/tests/built-lib.e2e.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/remotes/tests/built-lib.e2e.ts)
- [packages/client/connection/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/README.i18n.yaml)
- [packages/client/connection/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/README.md?plain=1)
- [packages/client/connection/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/README.zh.md?plain=1)
- [packages/client/connection/src/api-request-trust.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/api-request-trust.ts)
- [packages/client/connection/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/index.ts)
- [packages/client/connection/src/rpc-host.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/rpc-host.ts)
- [packages/client/connection/src/rpc.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/rpc.ts)
- [packages/client/connection/tests/fetch-routes.host.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/tests/fetch-routes.host.spec.ts)
- [packages/util/time/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/util/time/src/index.ts)

The **API Layer & Host-Client Bridge** provides the communication infrastructure between the Node.js host and the browser-based Web UI. It is designed to be transport-agnostic, type-safe, and capable of handling both unary RPC calls and complex event streaming.

Sources: [packages/client/connection/src/index.ts1-158](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/index.ts#L1-L158) [packages/api/gateway/src/client/index.ts1-140](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/src/client/index.ts#L1-L140)

### System Entity Map: Host to Client

Title: System Entity Map: Host to Client

Sources: [packages/client/connection/src/index.ts129-133](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/index.ts#L129-L133) [packages/api/gateway/src/client/index.ts142-183](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/src/client/index.ts#L142-L183)

---

## 5.1 API Proxy & RPC Protocol

For details, see [API Proxy & RPC Protocol](./5.1-api-proxy-and-rpc-protocol.md).

The `client-connection` package and `TypertGateway` form the central gateway on the host, exposing methods for session management, workspace organization, and host-level operations. `HostConnectionService` initializes browser authentication and HTTP transport routing [packages/client/connection/src/index.ts129-133](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/index.ts#L129-L133)

- **Wire Protocol**: Carries unary RPC calls and event streaming over structured endpoints [packages/client/connection/src/index.ts10-15](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/index.ts#L10-L15)
- **Validation & Security**: `BrowserAuth` manages signed cookies, while request trust validations check `Host` and `Origin` headers [packages/client/connection/src/index.ts11-12](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/index.ts#L11-L12)
- **Routing**: Exact routes and the `/api` HTTP bridge are managed via `HostConnectionService` [packages/client/connection/src/index.ts129-153](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/index.ts#L129-L153)

Sources: [packages/client/connection/src/index.ts129-153](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/index.ts#L129-L153)

---

## 5.2 Typert: Type-Safe RPC Generation

For details, see [Typert: Type-Safe RPC Generation](./5.2-typert:-type-safe-rpc-generation.md).

`Typert` generates "Host-for-Client" remote declarations, allowing host services decorated with `@Remote` or `@RemoteScope` to be exposed to the client with full type fidelity [docs/api-gateway.md7-16](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/api-gateway.md?plain=1#L7-L16)

- **Decorators**: Mark Cordis services and methods reachable over the bridge [docs/api-gateway.md7-13](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/api-gateway.md?plain=1#L7-L13)
- **Registry**: `TypertRegistry` maintains available remote endpoints on the host [docs/api-gateway.md86-88](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/api-gateway.md?plain=1#L86-L88)
- **Protocol**: Defines invocation descriptors and codecs ensuring correct serialization across the wire [docs/api-gateway.md84](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/api-gateway.md?plain=1#L84-L84)

Sources: [docs/api-gateway.md7-16](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/docs/api-gateway.md?plain=1#L7-L16)

---

## 5.3 Client Runtime & Session Management

For details, see [Client Runtime & Session Management](./5.3-client-runtime-and-session-management.md).

The browser-side client runtime translates raw RPC and multiplexed streams into state for the UI, managed by `ClientRemoteService` [packages/api/gateway/src/client/index.ts142-183](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/src/client/index.ts#L142-L183)

- **Connection Management**: `ConnectionController` and `ConnectionHandle` manage the connection lifecycle and exponential backoff [packages/api/gateway/src/client/index.ts167-173](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/src/client/index.ts#L167-L173)
- **ClientRemote Service**: Mounts `ctx.remote` in the browser, providing access to generated namespaces and multiplexed streams [packages/api/gateway/src/client/index.ts142-188](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/src/client/index.ts#L142-L188)
- **Host Facts**: Exposes identity-stable access to host information via `ctx.remote.$host` [packages/api/gateway/src/client/index.ts189-198](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/src/client/index.ts#L189-L198)

Sources: [packages/api/gateway/src/client/index.ts142-198](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/src/client/index.ts#L142-L198)

---

### Communication Flow Diagram

Title: Communication Flow Diagram

Sources: [packages/client/connection/src/index.ts129-153](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/client/connection/src/index.ts#L129-L153) [packages/api/gateway/src/client/index.ts142-183](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/api/gateway/src/client/index.ts#L142-L183)
