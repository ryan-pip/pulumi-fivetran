---
name: regenerate-sdks
description: Regenerate the schema and all four SDKs after a provider/resources.go change, bridge bump, or upstream terraform-provider-fivetran bump. Produces a clean diff suitable for a `chore: regenerate SDKs ...` commit.
---

# Regenerate SDKs

Use this when:

- You edited `provider/resources.go` (renamed/added a token, mapped a resource, etc.)
- You bumped `pulumi-terraform-bridge` in `provider/go.mod`
- You bumped `terraform-provider-fivetran` in `provider/go.mod`
- An upgrade bot opened a PR and you need to verify / extend it locally

## Steps

1. **Tidy Go modules first.** Stale module state is the #1 cause of "wide unrelated diffs" in the SDK output.

   ```bash
   cd provider && go mod tidy
   cd ..
   ```

2. **Rebuild tfgen and the schema.**

   ```bash
   make schema
   ```

   This regenerates `provider/cmd/pulumi-resource-fivetran/{schema.json,bridge-metadata.json,schema-embed.json}`. If `schema.json` is empty or has zero resources, stop — the bridge wiring in `provider/resources.go` is broken and that needs fixing first.

3. **Build all four SDKs in parallel-friendly order.** Each only depends on the schema sentinel:

   ```bash
   make build_sdks
   ```

   (Or one at a time: `make build_nodejs`, `make build_python`, `make build_go`, `make build_dotnet`.)

4. **Verify the worktree matches what CI will accept.** CI's `pull-request.yml` allows only this set of post-build dirty files:

   ```
   sdk/.*/pulumi-plugin\.json
   sdk/nodejs/package\.json
   sdk/python/pyproject\.toml
   sdk/go/.*/internal/pulumiUtilities\.go
   ```

   Quick local check:

   ```bash
   git status --porcelain | awk '{print $2}' \
     | grep -vE '^(sdk/.*/pulumi-plugin\.json|sdk/nodejs/package\.json|sdk/python/pyproject\.toml|sdk/go/.*/internal/pulumiUtilities\.go)$' \
     | grep -E '^sdk/' || echo "OK — only version-bearing files changed under sdk/"
   ```

   Anything else dirty under `sdk/` means the regen produced unexpected output.

5. **Smoke-test the Python SDK** (mocked, no Fivetran API needed):

   ```bash
   make test_python_smoke
   ```

6. **Commit.** Generated-only commits use the `chore: regenerate ...` prefix matching the existing history:

   ```bash
   git add provider/cmd/pulumi-resource-fivetran sdk/
   git commit -m "chore: regenerate schema + SDKs after <reason>"
   ```

   Don't bundle the regen commit with hand-written changes — keep them as separate commits on the same branch so reviewers can read the regen as a single mechanical diff.

## If the diff looks wrong

- **Huge unrelated comment changes**: ran without `go mod tidy` first. Reset and start at step 1.
- **Stale `setup.py` instead of `pyproject.toml`**: the Python codegen is producing an old shape — bridge or pulumictl version is too old. Don't hand-edit; fix the version (see commit `9a539ab`).
- **Doubled `v` in version strings**: `TFProviderVersion` includes a leading `v`. Strip it (commit `f1ea6e7`).
- **Provider binary rebuilds during a CI SDK shard**: `make --touch schema provider` is missing or out of order. The `make-targets` rule explains the file-target invariant.

## Don't

- Don't hand-edit anything under `sdk/` or `provider/cmd/pulumi-resource-fivetran/*.json` to "fix" output. Fix it upstream — in `provider/resources.go`, the bridge version, or the TF provider version — and re-tfgen.
- Don't skip step 1. It's the single most common source of noisy regen PRs in this repo's history.
