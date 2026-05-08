---
description: Bridge / upstream provider upgrades go in phased PRs (CI uplift → bridge → upstream → SDK regen). Regen commits must contain only generated files.
paths:
  - "provider/go.mod"
  - "provider/go.sum"
  - ".upgrade-config.yml"
  - ".github/workflows/upgrade-provider.yml"
---

# Bridge / Upstream Upgrade Flow

Phased, **one PR per concern**. The git history shows the pattern (e.g. `phase 0 repo + CI uplift`, `phase 2 — bridge v3.105.0 -> v3.127.0`, `phase 3 — terraform-provider-fivetran v1.0.3 -> v1.2.3`).

## Phases

1. **Repo / CI uplift** — anything that's not the dependency bump itself (workflows, Makefile, lint config). Do this first so subsequent regen PRs run on stable infra.
2. **Bridge bump** — `pulumi-terraform-bridge` version. Often pulls Go toolchain bumps with it.
3. **Upstream provider bump** — `terraform-provider-fivetran` version.
4. **Regenerate SDKs** — `make schema build_sdks`, commit the resulting diff under a `chore: regenerate SDKs ...` message. (Or use the `regenerate-sdks` skill.)

## Per phase

```bash
cd provider && go mod tidy
make sync-go-work    # bridge bumps may raise provider/go.mod's `go` directive
make schema build_sdks
git status           # confirm only the expected files changed
```

`make sync-go-work` aligns `go.work`'s `go` directive with the highest among the workspace modules. Skipping it leaves the workspace inconsistent and breaks `go vet`, `golangci-lint`, the provider build, and CodeQL autobuild on any PR that touched a module's `go` directive. The `upgrade-provider.yml` workflow runs the same sync automatically.

For regen commits, the diff should be **only** generated files. If you see hand-written changes too, split them into a separate commit on the same branch.

## Automated path

`pulumi-upgrade-provider-action` (called by `upgrade-provider.yml`) automates phases 2–4 as separate PRs with these branch prefixes — which is what the auto-merge filter keys off of:

- `upgrade-pulumi-terraform-bridge-*`
- `upgrade-terraform-provider-*`
- `upgrade-pulumi-version-*`

## When the bridge removes / renames a symbol

Don't paper over with a shim. Update `provider/resources.go` to the new bridge surface and re-tfgen. Memory `feedback_fix_dont_sidestep` applies: fix at the origin.

## When upstream removes a resource

The schema regen will drop it from `schema.json` and the SDKs. That's a breaking change for downstream Pulumi users — flag it in the PR description and bump a major version segment if appropriate (and you're not already pinned to `v0.x` "anything goes" semantics).
