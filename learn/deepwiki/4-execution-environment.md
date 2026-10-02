<!-- Source: https://deepwiki.com/deepseek-ai/deepseek-harness/4-execution-environment; extracted 2026-09-24 -->

# Execution Environment

Relevant source files

- [packages/fs/fs-local/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/README.i18n.yaml)
- [packages/fs/fs-local/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/README.md?plain=1)
- [packages/fs/fs-local/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/README.zh.md?plain=1)
- [packages/fs/fs-local/src/fsio.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/fsio.ts)
- [packages/fs/fs-local/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/index.ts)
- [packages/fs/fs-local/tests/filesystem.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/tests/filesystem.spec.ts)
- [packages/fs/fs-local/tests/fsio.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/tests/fsio.spec.ts)
- [packages/fs/fs/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs/README.i18n.yaml)
- [packages/fs/fs/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs/README.md?plain=1)
- [packages/fs/fs/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs/README.zh.md?plain=1)
- [packages/fs/fs/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs/src/index.ts)
- [packages/fs/fs/src/types.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs/src/types.ts)
- [packages/fs/fs/tests/service.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs/tests/service.spec.ts)
- [packages/fs/tool-fs/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/README.md?plain=1)
- [packages/fs/tool-fs/package.json](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/package.json)
- [packages/fs/tool-fs/src/edit.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/edit.ts)
- [packages/fs/tool-fs/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/index.ts)
- [packages/fs/tool-fs/src/read-render.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/read-render.ts)
- [packages/fs/tool-fs/src/read.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/read.ts)
- [packages/fs/tool-fs/src/session-cwd.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/session-cwd.ts)
- [packages/fs/tool-fs/src/write.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/write.ts)
- [packages/fs/tool-fs/tests/integration.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/tests/integration.spec.ts)
- [packages/fs/tool-fs/tests/read-render.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/tests/read-render.spec.ts)
- [packages/fs/tool-fs/tests/tools.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/tests/tools.spec.ts)
- [packages/subprocess/subprocess-local/README.i18n.yaml](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/README.i18n.yaml)
- [packages/subprocess/subprocess-local/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/README.md?plain=1)
- [packages/subprocess/subprocess-local/README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/README.zh.md?plain=1)
- [packages/subprocess/subprocess-local/src/index.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/index.ts)
- [packages/subprocess/subprocess-local/src/linux-scope.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/linux-scope.ts)
- [packages/subprocess/subprocess-local/src/managed-owner.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/managed-owner.ts)
- [packages/subprocess/subprocess-local/src/runner-launch.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/runner-launch.ts)
- [packages/subprocess/subprocess-local/src/spawn-runner.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/spawn-runner.ts)
- [packages/subprocess/subprocess-local/src/spawn.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/spawn.ts)
- [packages/subprocess/subprocess-local/src/windows-job.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/windows-job.ts)
- [packages/subprocess/subprocess-local/tests/linux-scope.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/tests/linux-scope.spec.ts)
- [packages/subprocess/subprocess-local/tests/local.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/tests/local.spec.ts)
- [packages/subprocess/subprocess-local/tests/native-containment.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/tests/native-containment.spec.ts)
- [packages/subprocess/subprocess-local/tests/native-windows.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/tests/native-windows.spec.ts)
- [packages/subprocess/subprocess-local/tests/spawn-runner.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/tests/spawn-runner.spec.ts)
- [packages/subprocess/subprocess-local/tests/spawn.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/tests/spawn.spec.ts)
- [packages/subprocess/subprocess-local/tests/windows-job.spec.ts](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/tests/windows-job.spec.ts)

The **Execution Environment** in `dsh` manages how the system interacts with the host filesystem, spawns native processes, applies security policies, and distributes native platform binaries. It is built on the **Capability Seam** pattern, where high-level tools and agents interact with abstract interfaces (`ctx.fs`, `ctx.subprocess`, `ctx.sandbox`) that are fulfilled by specific provider plugins (e.g., `LocalFileSystem`, `LocalSubprocessRuntime`).

This is a parent overview page. For granular details on specific sub-topics, see the child pages:

- [Filesystem Tools & Observation](./4.1-filesystem-tools-and-observation.md)
- [Shell, Subprocess & Terminal](./4.2-shell-subprocess-and-terminal.md)
- [Sandboxing & Security](./4.3-sandboxing-and-security.md)
- [Native System Packages & Platform Binaries](./4.4-native-system-packages-and-platform-binaries.md)

### Core Subsystems

| Area | Responsibility | Primary Services & Modules |
| --- | --- | --- |
| **Filesystem** | File I/O, atomic writes, and observation tracking. | `FileSystem` [packages/fs/fs/src/index.ts25-27](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs/src/index.ts#L25-L27) `LocalFileSystem` [packages/fs/fs-local/src/index.ts64](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/index.ts#L64-L64) `fsio.ts` [packages/fs/fs-local/src/fsio.ts1-152](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/fsio.ts#L1-L152) |
| **Subprocess** | Shell execution, PTY management, and process trees. | `SubprocessRuntime` [packages/subprocess/subprocess/src/index.ts23](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess/src/index.ts#L23-L23) `LocalSubprocessRuntime` [packages/subprocess/subprocess-local/src/index.ts37](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/index.ts#L37-L37) |
| **Sandboxing** | Resource restriction, Landlock, and security policies. | `SandboxProvider` [packages/sandbox/sandbox/src/index.ts37](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/sandbox/sandbox/src/index.ts#L37-L37) `sandbox-windows-acl` [packages/sandbox/sandbox-windows-acl/src/index.ts1-130](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/sandbox/sandbox-windows-acl/src/index.ts#L1-L130) |
| **Native Packages** | Platform binaries, launchers, and prebuilt addons. | `native/` sub-workspace, launcher binary, `flock` addon. |

### System Architecture: From Tools to OS

The following diagram illustrates how natural language tool calls from an agent are translated into concrete OS-level operations through the capability seams, bridging natural language spaces to concrete code entities.

**Tool-to-Entity Mapping**

Sources: [packages/fs/tool-fs/src/read.ts136-163](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/read.ts#L136-L163) [packages/subprocess/subprocess-local/src/index.ts146-157](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/index.ts#L146-L157) [packages/fs/fs-local/src/index.ts64-77](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/index.ts#L64-L77)

---

## 4.1 Filesystem Tools & Observation

The filesystem layer provides a unified interface for file operations with a focus on safety, version tracking, and observation policies. All writes are performed via a "write-then-rename" pattern in private sibling directories to prevent partial file corruption [packages/fs/fs-local/src/fsio.ts2-5](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/fsio.ts#L2-L5) Files are resolved to realpath-based target keys to ensure symlinks share state correctly [packages/fs/fs-local/src/fsio.ts106-111](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/fsio.ts#L106-L111) Furthermore, observation policies track reads and edits via `fs/observed` events to enforce correctness constraints [packages/fs/tool-fs/src/read.ts162](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/read.ts#L162-L162)

For details on fs capability seams, local providers, search utilities, and the string-replace editor, see [Filesystem Tools & Observation](./4.1-filesystem-tools-and-observation.md).

Sources: [packages/fs/fs-local/src/fsio.ts1-152](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/fsio.ts#L1-L152) [packages/fs/tool-fs/src/read.ts136-163](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/read.ts#L136-L163)

---

## 4.2 Shell, Subprocess & Terminal

`dsh` manages processes as detached process trees to ensure that descendant processes do not outlive their parent handles [packages/subprocess/subprocess-local/src/spawn.ts2-6](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/spawn.ts#L2-L6) The local subprocess runtime integrates POSIX process groups and Windows Job objects, supports persistent PTY sessions via `node-pty`, and captures process output with bounded in-memory tails and spill files [packages/subprocess/subprocess-local/src/spawn.ts126-143](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/spawn.ts#L126-L143) Additionally, it hooks into Node's `exit` event to guarantee synchronous cleanup of orphaned processes [packages/subprocess/subprocess-local/src/index.ts49-59](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/index.ts#L49-L59)

For details on local spawning, PTY sessions, terminal tools, and the E2B cloud sandbox backend, see [Shell, Subprocess & Terminal](./4.2-shell-subprocess-and-terminal.md).

Sources: [packages/subprocess/subprocess-local/src/index.ts37-157](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/index.ts#L37-L157) [packages/subprocess/subprocess-local/src/spawn.ts1-161](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/spawn.ts#L1-L161)

---

## 4.3 Sandboxing & Security

The execution environment enforces strict security boundaries by default. On Linux, it uses `Landlock` via native addons to restrict filesystem access [packages/sandbox/sandbox-local/src/index.ts28-33](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/sandbox/sandbox-local/src/index.ts#L28-L33); on Windows, it employs restricted security tokens and DACL isolation [packages/sandbox/sandbox-windows-acl/src/index.ts3-13](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/sandbox/sandbox-windows-acl/src/index.ts#L3-L13) High-risk operations are also gated by user approval flows (`ctx.approval`) [packages/fs/tool-fs/README.md66-69](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/README.md?plain=1#L66-L69) and subprocesses execute within credential-scrubbed environments [packages/subprocess/subprocess-local/src/spawn.ts43-53](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/spawn.ts#L43-L53)

For details on sandbox policies, Landlock rules, and Windows ACLs, see [Sandboxing & Security](./4.3-sandboxing-and-security.md).

Sources: [packages/sandbox/sandbox-windows-acl/src/index.ts1-130](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/sandbox/sandbox-windows-acl/src/index.ts#L1-L130)

---

## 4.4 Native System Packages & Platform Binaries

The `native/` sub-workspace houses platform-specific binaries, including launcher executables, the `flock` native addon, and prebuilt packages targeting `linux` and `darwin` across `x64` and `arm64` architectures. These packages define strict CLI and flock contracts and supply the release scripts required for packing and publishing.

For details on platform prebuilds, launcher binaries, and release packaging, see [Native System Packages & Platform Binaries](./4.4-native-system-packages-and-platform-binaries.md).

Sources: [packages/subprocess/subprocess-local/README.md10-57](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/README.md?plain=1#L10-L57)

---

### Execution Lifecycle

The following diagram shows the lifecycle of a subprocess managed by `LocalSubprocessRuntime`, including how it handles clean teardown during host exit.

**Subprocess Lifecycle & Cleanup**

Sources: [packages/subprocess/subprocess-local/src/index.ts49-60](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/index.ts#L49-L60) [packages/subprocess/subprocess-local/src/index.ts79-102](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/index.ts#L79-L102) [packages/subprocess/subprocess-local/src/spawn.ts169-181](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/spawn.ts#L169-L181)

**Sources:**

- [packages/fs/fs-local/src/fsio.ts1-152](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/fsio.ts#L1-L152)
- [packages/subprocess/subprocess-local/src/index.ts37-157](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/index.ts#L37-L157)
- [packages/fs/fs-local/src/index.ts64-171](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/fs-local/src/index.ts#L64-L171)
- [packages/fs/tool-fs/src/read.ts136-163](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/fs/tool-fs/src/read.ts#L136-L163)
- [packages/subprocess/subprocess-local/src/spawn.ts1-161](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/src/spawn.ts#L1-L161)
- [packages/sandbox/sandbox-windows-acl/src/index.ts1-130](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/sandbox/sandbox-windows-acl/src/index.ts#L1-L130)
- [packages/subprocess/subprocess-local/README.md10-57](https://github.com/deepseek-ai/deepseek-harness/blob/ddefc45f/packages/subprocess/subprocess-local/README.md?plain=1#L10-L57)
