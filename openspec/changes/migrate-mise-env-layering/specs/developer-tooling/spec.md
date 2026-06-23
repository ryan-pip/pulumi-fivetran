## ADDED Requirements

### Requirement: Config-environment mise layout
The repo SHALL use `mise.toml` (the lean base/CI toolchain), `mise.dev.toml` (dev-only additive tools and env), and `.miserc.toml` (`env = ["dev", "local"]`) so local installs layer dev (and any per-user `mise.local.toml`) on top of the base by default. The repo SHALL NOT contain a `mise.ci.toml` or a `setup-mise` composite action. `[settings] lockfile = true` SHALL be set and the committed lockfiles (`mise.lock` for base, `mise.dev.lock` for dev) SHALL be kept in sync via `mise lock`.

#### Scenario: CI loads only the base toolchain
- **WHEN** a workflow runs with `MISE_ENV=ci`
- **THEN** mise installs only the tools in `mise.toml` and `mise.dev.toml` is not loaded

#### Scenario: local dev loads base plus dev
- **WHEN** a developer runs `mise install` with no `MISE_ENV` override
- **THEN** `.miserc.toml` causes `mise.dev.toml` (and `mise.local.toml` if present) to layer on top of `mise.toml`

#### Scenario: tool versions are pinned by lockfiles
- **WHEN** CI and a developer install the same config environment
- **THEN** they resolve identical tool versions from the committed `mise.lock` / `mise.dev.lock`
