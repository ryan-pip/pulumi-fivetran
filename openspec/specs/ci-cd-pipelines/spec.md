# ci-cd-pipelines Specification

## Purpose
TBD - created by archiving change migrate-mise-env-layering. Update Purpose after archive.
## Requirements
### Requirement: Workflows install mise directly
Every workflow SHALL install the toolchain by calling `jdx/mise-action` directly (no composite wrapper) with `MISE_ENV: ci` set, SHALL NOT pin the mise CLI version (no `version:` input), and SHALL use the cache key `mise-{{platform}}-{{file_hash}}` (without `{{version}}`). `cache_save` SHALL be `true` on exactly one job per workflow and restore-only on the rest.

#### Scenario: CI installs the base set without the wrapper
- **WHEN** any of pull-request, release, or upgrade-provider runs its mise step
- **THEN** it invokes `jdx/mise-action` directly, installs the base set, and shares the `mise-{{platform}}-{{file_hash}}` cache

#### Scenario: cache survives mise CLI releases
- **WHEN** a new mise CLI version is released but the lockfiles are unchanged
- **THEN** the cache key is unchanged and the warm cache is restored

### Requirement: Upgrade-provider runs on the base toolchain
The scheduled `upgrade-provider` workflow SHALL run on the base set (`MISE_ENV: ci`), SHALL install the `upgrade-provider` binary itself via `go install`, and SHALL set `cache_save: true`. It SHALL NOT load the dev set, because the repo builds only nodejs/python/go/dotnet SDKs (all present in the base) and does not invoke gopls/hk/linters. The existing `Sync go.work go directive` step SHALL be preserved.

#### Scenario: the upgrade workflow installs mise successfully
- **WHEN** the scheduled `upgrade-provider` workflow runs its `Setup mise` step
- **THEN** it installs only the base set (no `gopls`/`node` full-set failures) and proceeds to run `upgrade-provider`

#### Scenario: the upgrade workflow populates the cache
- **WHEN** the single-job upgrade workflow installs mise
- **THEN** `cache_save: true` writes the toolchain cache for subsequent runs

### Requirement: node is exact-pinned for the upgrade flow
`node` SHALL be pinned to an exact version in base `mise.toml` (≥ 24.1). `upgrade-provider` runs `mise upgrade --raw`, which re-resolves each tool's spec outside the lockfile; a fuzzy `node` spec causes a fresh node install via its gpg-signature path, which fails on GitHub-hosted runners. An exact pin makes `mise upgrade` a no-op for node so it is never reinstalled. `pulumi` SHALL NOT be exact-pinned (exact pins have caused issues and there is no automated mise-pin bump); non-gpg tools may stay fuzzy.

#### Scenario: mise upgrade does not reinstall node
- **WHEN** the upgrade workflow runs `upgrade-provider`, which invokes `mise upgrade --raw`
- **THEN** node's exact pin matches the installed version, so node is not reinstalled and its gpg verification never runs

#### Scenario: the go.work sync step is retained
- **WHEN** the upgrade workflow rewrite lands
- **THEN** the `Sync go.work go directive` step remains in `upgrade-provider.yml`, gated on the upgrade-branch prefixes

### Requirement: Upgrade-provider uses this repo's own bot identity
`upgrade-provider.yml` SHALL reference this repo's release-bot GitHub App identity — the app that mints the token via `actions/create-github-app-token` — derived dynamically from that step's `app-slug` output, in both places the bot identity appears, and SHALL NOT hardcode the upstream `pulumi-release-bot` identity in either:
- The `Set up git identity` step SHALL be retained (git requires a committer identity to make the upgrade commit(s) and push the PR branch) and SHALL set `user.name = "<app-slug>[bot]"` with the matching noreply `user.email`.
- The `Enable auto-merge on upgrade PR` step's author safety filter SHALL compare against `app/<app-slug>` for this repo's app.

#### Scenario: commits are attributed to this repo's bot
- **WHEN** the upgrade workflow configures git identity
- **THEN** `user.name` is `<app-slug>[bot]` for this repo's app and `user.email` is the matching `<bot-user-id>+<app-slug>[bot]@users.noreply.github.com`, not `pulumi-release-bot[bot]`

#### Scenario: auto-merge accepts this repo's bot as author
- **WHEN** the `Enable auto-merge on upgrade PR` step checks the PR author
- **THEN** it matches `app/<app-slug>` for this repo's app and enables auto-merge, rather than skipping because the author is not `app/pulumi-release-bot`

### Requirement: Auto-tag uses this repo's own bot identity

`auto-tag.yml` (the `auto-tag-upstream-bump` workflow) SHALL attribute the mirror tags it pushes to this repo's release-bot GitHub App identity — the app that mints the token via `actions/create-github-app-token` — derived dynamically from that step's `app-slug` output, and SHALL NOT hardcode the upstream `pulumi-release-bot` identity. The `Push tag` step SHALL set `user.name = "<app-slug>[bot]"` with the matching noreply `user.email` of the form `<bot-user-id>+<app-slug>[bot]@users.noreply.github.com`, where `<bot-user-id>` is resolved from the GitHub API for that bot user. The step SHALL pass the minted app token as `GH_TOKEN` so the API lookup is authenticated. This mirrors the identity derivation already required of `upgrade-provider.yml`.

#### Scenario: tags are attributed to this repo's bot

- **WHEN** the `auto-tag-upstream-bump` workflow configures git identity before pushing a mirror tag
- **THEN** `user.name` is `<app-slug>[bot]` for this repo's app and `user.email` is the matching `<bot-user-id>+<app-slug>[bot]@users.noreply.github.com`, not `pulumi-release-bot[bot]`

#### Scenario: the bot-user-id lookup is authenticated

- **WHEN** the `Push tag` step resolves the bot user's id via `gh api`
- **THEN** the step has `GH_TOKEN` set to the minted app token so the lookup succeeds

