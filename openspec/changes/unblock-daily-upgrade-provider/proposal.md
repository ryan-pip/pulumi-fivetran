# Unblock daily upgrade-provider: Go toolchain drift

## Why

The scheduled `upgrade-provider` workflow has failed every day since 2026-07-11. `mise.toml` `[env]` hard-pins `GOTOOLCHAIN = "go1.25.9"` — a second, hand-maintained copy of the Go version that `mise.lock` already pins (currently go 1.25.11). Bridge v3.134.0 declares `go >= 1.25.11`, so the workflow's `go get pulumi-terraform-bridge/v3` hard-fails: `requires go >= 1.25.11 (running go 1.25.9; GOTOOLCHAIN=go1.25.9)`. Because mise shims re-export `[env]` over the caller's environment, the pin is absolute in CI. The pin has needed hand bumps repeatedly; the failure class recurs every time the bridge adopts a newer Go patch release. (Sibling change of the same name in pulumi-astronomer, which additionally has a C# codegen collision; this repo needs only the toolchain fix — its upstream has no pending tag.)

## What Changes

- Replace `GOTOOLCHAIN = "go1.25.9"` with `GOTOOLCHAIN = "auto"` in `mise.toml` `[env]`, removing the duplicated exact Go version. `mise.lock` stays the single pinned source of the installed toolchain; module `go` directives (managed by `go get`/upgrade-provider and the workflow's go.work sync step) declare the minimum, and Go resolves/downloads a newer checksummed toolchain only when a module requires it. Verified in the astronomer sibling (identical mise layout, same bridge target): with `auto`, `go get pulumi-terraform-bridge/v3@v3.134.0` succeeds, bumps the module `go` directive to 1.25.11, and the workspace builds.

## Capabilities

### New Capabilities

(none)

### Modified Capabilities

- `developer-tooling`: new requirement — the mise env SHALL NOT hard-pin an exact Go toolchain (`GOTOOLCHAIN` = exact version). Toolchain selection SHALL be `auto` so the exact installed version is pinned in one place (`mise.lock`) and module `go` directives can pull a newer toolchain without manual intervention.

## Impact

- `mise.toml` (`[env]` block) — one-line change; affects every mise-run Go invocation (CI and dev).
- No workflow YAML changes. The existing `Sync go.work go directive` step already handles the directive skew the bridge bump creates.
- Risk note: with `auto`, CI may download a Go toolchain newer than `mise.lock`'s (checksummed via the Go toolchain sumdb, recorded in committed `go` directives). `mise.lock` and `golangci-lint` should still be bumped periodically (`mise up`), but a stale lockfile no longer breaks the daily automation.
