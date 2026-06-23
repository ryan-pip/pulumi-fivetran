## Why

The scheduled `Upgrade provider` workflow has failed every day, dying in the `Setup mise` step ~3 minutes in — before `upgrade-provider` ever runs. Root cause: this workflow is the only one that calls `jdx/mise-action` directly against the repo-root `mise.toml` (the **full** dev tool set), while every other workflow (pull-request, release) installs the trimmed `mise.ci.toml` via the `./.github/actions/setup-mise` composite wrapper. The full set drags in two tools that fail to install — `go:golang.org/x/tools/gopls@latest` (build failure under the pinned `GOTOOLCHAIN`) and `core:node@22` (fresh GPG verification, never cached because `cache_save: false`) — and the whole step exits 1.

The current `mise.toml` (full) + `mise.ci.toml` (trimmed copy) + composite-wrapper arrangement is brittle: it maintains two parallel tool lists and a wrapper whose only job is to stage the CI config into `$RUNNER_TEMP` so `mise-action` reads it instead of the full file. The kai/madi fleet has since standardized on mise's native **config-environment layering**: a lean base `mise.toml`, an additive `mise.dev.toml`, and a committed `.miserc.toml` (`env = ["dev", "local"]`) so dev is the local default and CI opts out with `MISE_ENV=ci`. This drops the wrapper and the parallel file entirely.

## What Changes

- **Invert the mise layout.** `mise.toml` becomes the lean **base/CI** set (today's `mise.ci.toml` contents); a new `mise.dev.toml` carries the **dev-only** delta (java, gopls, hk, pkl, yamllint, taplo, actionlint, the `upgrade-provider` binary); a new `.miserc.toml` sets `env = ["dev", "local"]` so local installs layer dev+local automatically. Delete `mise.ci.toml`.
- **Drop the wrapper.** Delete `./.github/actions/setup-mise`. Every workflow calls `jdx/mise-action` directly with `MISE_ENV: ci` so it installs only the base set.
- **Drop the mise CLI version pin.** Remove the `version: 2026.3.7` input; the action installs latest mise. The cache key is **unchanged** (`mise-{{platform}}-{{file_hash}}`, no `{{version}}`) so the cache stays warm across mise CLI releases; tool versions stay pinned by the committed lockfiles until they're regenerated.
- **Commit mise lockfiles.** Generate and commit `mise.lock` (base) and `mise.dev.lock` (dev) via `mise lock` so CI and dev resolve identical tool versions.
- **Fix the upgrade workflow.** `upgrade-provider.yml` runs on the **base** set (`MISE_ENV: ci`) like every other workflow — the Makefile builds only nodejs/python/go/dotnet SDKs, all in the base, and the workflow installs the `upgrade-provider` binary itself via `go install`. Set `cache_save: true` (it is the only job, so it must populate the cache). The existing `Sync go.work go directive` step is preserved.

## Capabilities

### New Capabilities
- `developer-tooling`: how this repo defines dev/CI tool versions via the mise config-environment layout (base/dev layering + lockfiles).
- `ci-cd-pipelines`: how the GitHub Actions workflows install that toolchain and run the scheduled `upgrade-provider` job. (CD/release requirements can land here in future.)

## Impact

- New: `mise.dev.toml`, `.miserc.toml`, `mise.dev.lock`.
- Modified: `mise.toml` (now base), `mise.lock` (regenerated), `.github/workflows/pull-request.yml`, `.github/workflows/release.yml`, `.github/workflows/upgrade-provider.yml`.
- Removed: `mise.ci.toml`, `.github/actions/setup-mise/`.
- CI/dev tooling only — no provider runtime or SDK behavior change.
- Part of the two-repo effort to give `pulumi-astronomer` and `pulumi-fivetran` the same upgrade-provider/mise pattern; each carries its own repo-local change.

## Out of scope

- The `Sync go.work go directive` step is already present in this repo's `upgrade-provider.yml` and is retained as-is; the equivalent step is being added to `pulumi-astronomer` under a separate follow-up so the two upgrade workflows fully match.
