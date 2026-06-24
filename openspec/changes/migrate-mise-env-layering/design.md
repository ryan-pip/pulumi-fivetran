## Context

`pulumi-fivetran` is a Pulumi terraform-bridge provider (Go provider + nodejs/python/go/dotnet SDKs). It uses `mise` for toolchain management. Today: `mise.toml` holds the full dev tool set; `mise.ci.toml` is a hand-maintained trimmed copy; a `./.github/actions/setup-mise` composite action stages `mise.ci.toml` into `$RUNNER_TEMP/mise-ci` and runs `jdx/mise-action` there so CI installs only the subset. `upgrade-provider.yml` bypassed all of this and called `jdx/mise-action` against the full repo-root `mise.toml`, which is why it failed daily.

## Goals / Non-Goals

**Goals:**
- One mise layout (base + dev + `.miserc.toml`), no parallel `mise.ci.toml`, no composite wrapper.
- CI (incl. the upgrade workflow) installs the lean base set directly via `jdx/mise-action` + `MISE_ENV: ci`.
- Identical pattern to `pulumi-astronomer`.

**Non-Goals:**
- Changing tool *versions* (the base set keeps today's `mise.ci.toml` versions; dev keeps today's full-set versions).
- Any change to provider/SDK build behavior.
- The existing `Sync go.work go directive` step — it is preserved unchanged.

## Decisions

- **Config-environment layering.** mise loads `mise.toml` always; `.miserc.toml` (`env = ["dev", "local"]`) makes mise additionally load `mise.dev.toml` + `mise.local.toml` locally by default. CI sets `MISE_ENV=ci`, which overrides that list, so only `mise.toml` loads. This is additive-only (mise can't subtract), which is why base must be the *lean* set and dev the *extras* — the inverse of today.

- **Base `mise.toml`** (= today's `mise.ci.toml`):
  ```toml
  [settings]
  experimental = true
  fetch_remote_versions_cache = "24h"
  http_retries = 3
  lockfile = true

  [tools]
  go = "1.25"
  node = "22"
  python = "3.11"
  dotnet = "8.0"
  pulumi = "3"
  uv = "latest"
  golangci-lint = "2"
  "go:github.com/pulumi/pulumictl/cmd/pulumictl" = "latest"

  [env]
  GOTOOLCHAIN = "go1.25.9"
  ```
  `github-cli` is intentionally **not** in base: `gh` is preinstalled on GitHub-hosted runners, and it's used only by `upgrade-provider.yml` (ubuntu-latest). It lives in `mise.dev.toml` for local parity.

- **`mise.dev.toml`** (the delta vs. today's full `mise.toml`):
  ```toml
  [settings]
  experimental = true   # required for the go: backends below

  [tools]
  github-cli = "latest"
  java = "corretto-11"
  "go:golang.org/x/tools/gopls" = "latest"
  "go:github.com/pulumi/upgrade-provider" = "main"
  hk = "latest"
  pkl = "latest"
  yamllint = "latest"
  taplo = "latest"
  actionlint = "latest"

  [env]
  HK_MISE = 1
  ```

- **`.miserc.toml`**: `env = ["dev", "local"]`.

- **Lockfiles.** Run `mise lock` to produce committed `mise.lock` (base) and `mise.dev.lock` (dev). With `lockfile = true`, each config file gets its own lock so CI and dev resolve identical versions.

- **Workflow mise step** (all of pull-request / release / upgrade-provider): `MISE_ENV: ci` at the workflow `env:` block, and inline:
  ```yaml
  - name: Setup mise
    uses: jdx/mise-action@<pinned-sha>   # action sha stays pinned; mise CLI version no longer pinned
    env:
      MISE_FETCH_REMOTE_VERSIONS_TIMEOUT: 30s
    with:
      cache_save: ${{ <true on exactly one job per workflow> }}
      cache_key: "mise-{{platform}}-{{file_hash}}"
  ```
  No `version:` input (mise CLI floats to latest). Cache key keeps the existing `mise-{{platform}}-{{file_hash}}` form (no `{{version}}`) so it survives near-daily mise releases; tool versions are pinned by the lockfiles.

- **`cache_save` placement.** Multi-job workflows (pull-request, release) keep `cache_save: true` on exactly the one prerequisites/build job that today sets it on the wrapper; all other jobs restore only. The single-job `upgrade-provider` sets `cache_save: true` (was `false` — the reason it never cached and re-ran the brittle fresh `node@22`/`gopls` installs every day).

- **upgrade-provider on the base set.** Verified via the Makefile: `build_sdks = build_nodejs build_python build_go build_dotnet` (no Java SDK), and gopls/hk/linters are never invoked. So `upgrade-provider --kind=all` needs only the base toolchain; the `upgrade-provider` binary is installed in its own `go install ...@main` step. Loading the full set was the cause of the failure, not a requirement.

- **`Sync go.work go directive` step retained.** This repo's `upgrade-provider.yml` has an extra step that bumps `go.work`'s `go` directive after a bridge upgrade. It is independent of the mise change and is preserved unchanged (still gated on the upgrade-branch prefixes).

## Risks / Trade-offs

- **`{{file_hash}}` scope.** With the wrapper gone, `mise-action` computes `{{file_hash}}` from the mise config/lock in the working directory (repo root). Under `MISE_ENV=ci` only `mise.toml`/`mise.lock` are active. Confirm during apply that the cache key resolves consistently and the cache is shared across the three workflows.
- **Latest mise CLI.** Dropping the version pin means a bad mise release could surface in CI before the lockfiles change. Accepted per the fleet pattern; the file-hash cache key isolates the toolchain from CLI churn.
- **First run after merge** repopulates the cache (cold) on the `cache_save` job; subsequent runs restore.
