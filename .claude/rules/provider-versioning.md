---
description: Provider version comes from `pulumictl get version -o` (the `-o` is mandatory for PyPI). Pre-release tag handling for GoReleaser, npm, and GitHub release. Pull-before-tag rule.
paths:
  - "Makefile"
  - ".github/workflows/release.yml"
  - ".github/workflows/pull-request.yml"
  - ".goreleaser.yml"
  - "provider/pkg/version/**"
---

# Provider Versioning

## Source of truth

Provider version comes from git tags, resolved by `pulumictl get version -o`:

- `-o` produces a SemVer-compatible version (no `+<sha>` build metadata).
- PyPI rejects local-version metadata, so `-o` is **mandatory** for the Python SDK build.
- Local builds default to `PROVIDER_VERSION=1.0.0-alpha.0+dev` (see Makefile).

## In CI

Every job that needs the version sets it itself:

```yaml
- name: Set provider version
  run: echo "PROVIDER_VERSION=$(pulumictl get version -o)" >> "$GITHUB_ENV"
```

Don't try to share `$PROVIDER_VERSION` between jobs via artifact — re-running `pulumictl` is cheap and avoids stale-value bugs.

## Pre-release tags (`vX.Y.Z-rc1`, `vX.Y.Z-alpha.1`)

- **GoReleaser**: `GORELEASER_CURRENT_TAG=${GITHUB_REF_NAME}` (the literal pushed tag) — pulumictl's `+<sha>` metadata fails GoReleaser's tag-equals-ref validation.
- **npm**: published with `--tag next`, not `latest`.
- **GitHub release**: `prerelease: ${{ contains(github.ref_name, '-') }}`.

## Before tagging

Always `git pull --ff-only origin main` immediately before `git tag` on a shared branch — see memory `feedback_pull_before_tag`. Re-confirm HEAD with `git log -1 --oneline` before pushing the tag.

## Don't

- Hand-edit version strings in generated `sdk/python/pyproject.toml`, `sdk/nodejs/package.json`, `sdk/go/.../pulumiUtilities.go`, `sdk/dotnet/version.txt` — they're regenerated from `PROVIDER_VERSION` on every build.
- Strip the `v` prefix from the tag for `TFProviderVersion` — `f1ea6e7` showed that doubles the `v` in the SDK.
