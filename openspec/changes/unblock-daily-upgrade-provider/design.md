# Design — unblock-daily-upgrade-provider (fivetran)

## Context

Mirror of the pulumi-astronomer change of the same name; see that repo's `openspec/changes/unblock-daily-upgrade-provider/design.md` for the full diagnosis and verification record. Summary: the daily `upgrade-provider` job fails at `go get pulumi-terraform-bridge/v3` because bridge v3.134.0 requires go ≥ 1.25.11 while `mise.toml` `[env]` pins `GOTOOLCHAIN = "go1.25.9"` — an exact-version duplicate of what `mise.lock` pins (go 1.25.11) that has drifted. mise shims re-export `[env]` over the caller's environment, so the pin cannot be overridden per-step. This repo has no second failure: upstream `terraform-provider-fivetran` has no pending tag (the failing runs never enter the `Update TF Provider` phase).

## Goals / Non-Goals

**Goals:** daily automation green; one pinned source of the installed Go version (`mise.lock`); no recurrence when the bridge next adopts a Go patch release.

**Non-Goals:** workflow YAML changes; bumping bridge/upstream by hand (the bot does that once unblocked).

## Decisions

### D1: `GOTOOLCHAIN = "auto"` (not `local`, not a fresher exact pin)

Same decision and rationale as the astronomer sibling: an exact pin recreates this incident on next drift; `local` still hard-fails whenever the bridge requires newer Go than the lockfile (nothing automated bumps `mise.lock`); `auto` satisfies future requirements by downloading the exact sumdb-checksummed toolchain, with the requirement recorded in committed `go` directives. Verified against bridge v3.134.0 in the astronomer worktree (identical mise layout and pin).

## Risks / Trade-offs

Same as the sibling: [toolchain may be downloaded newer than mise.lock's] → checksummed, directive-pinned in git, re-synced by periodic `mise up`; [golangci-lint lagging a new Go language version] → pre-existing under any setting, surfaces as a red PR check.

## Migration Plan

1. One-line PR changing the mise env value.
2. Next scheduled run should open the bridge v3.134.0 upgrade PR (go directive bump + go.work sync included) and auto-merge per the existing safety filters.
3. Rollback: revert the line.

## Open Questions

None.
