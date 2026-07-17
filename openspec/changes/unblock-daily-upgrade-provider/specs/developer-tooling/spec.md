# developer-tooling — delta for unblock-daily-upgrade-provider

## ADDED Requirements

### Requirement: Go toolchain selection is not exact-pinned in mise env

The mise `[env]` block SHALL set `GOTOOLCHAIN = "auto"` and SHALL NOT pin `GOTOOLCHAIN` to an exact Go version. The exact installed Go version SHALL be pinned in exactly one place — `mise.lock` — and module `go` directives (`provider/go.mod`, `provider/shim/go.mod`, `sdk/go.mod`, `go.work`) SHALL declare minimum-version requirements that the go command MAY satisfy by downloading a newer checksummed toolchain than the one mise installed.

#### Scenario: bridge requires a newer Go than the installed toolchain

- **WHEN** the daily upgrade workflow runs `go get github.com/pulumi/pulumi-terraform-bridge/v3@<new>` whose module declares `go >= X` with X newer than the mise-installed Go
- **THEN** the go command resolves and downloads toolchain X automatically, the `go get` succeeds, and the `go` directive bump lands in the upgrade PR instead of the workflow hard-failing

#### Scenario: installed toolchain satisfies the requirement

- **WHEN** every module's `go` directive is satisfied by the mise-installed Go from `mise.lock`
- **THEN** the go command uses the mise-installed toolchain with no download

#### Scenario: no second copy of the Go version can drift

- **WHEN** `mise.lock`'s Go version is bumped (e.g. by `mise up`)
- **THEN** no other file in the repo holds an exact Go toolchain version that must be bumped in lockstep (`grep -r "GOTOOLCHAIN" mise*.toml` shows only `auto`)
