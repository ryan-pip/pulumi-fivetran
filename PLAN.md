# Plan: Automate Provider Updates + Quality Uplift for pulumi-fivetran

**Last updated**: 2026-04-16  
**Working branch**: `claude/automate-provider-updates-2DiaM`

---

## Status Summary

| Phase | Description | Status |
|---|---|---|
| Phase 0 | Repo uplift (lint, tests, schema validation CI) | **DONE — needs PR + merge** |
| Phase 1 | Delete 14 stale branches | Not started |
| Phase 2 | Bridge upgrade v3.111.0 → v3.126.0 | Not started (blocked on Phase 0 merge) |
| Phase 3 | Provider upgrade v1.9.4 → v1.9.29 | Not started (blocked on Phase 2 merge) |

---

## Phase 0 — Repo Uplift ✅ COMPLETE (on branch, no PR yet)

All changes are committed on `claude/automate-provider-updates-2DiaM` (4 commits ahead of main).
**Next action**: Create a PR from this branch to `main`, get it merged.

### What was done

**`.golangci.yml`** — Rewrote for golangci-lint v2 format. Removed 6 deprecated linters
(`megacheck`, `deadcode`, `structcheck`, `varcheck`, `golint`, `interfacer`), replaced with
modern equivalents (`staticcheck`, `unused`, `revive`). Added `exclude-dirs: [cmd]` because
`cmd/` embeds `schema-embed.json` which is only present after `make generate`.

**`.github/workflows/pull-request.yml`** — Added three new jobs:
- `lint`: installs golangci-lint v2.5.0 via shell script, runs on `provider/` and `provider/pkg/...`
- `unit_test`: runs `go vet` and `go test -v -short -parallel 10` (excludes `cmd/`)
- `schema_validation`: validates `schema.json` is valid JSON and has > 0 resources
Also bumped `actions/setup-go` from v4 → v5.

**`.github/workflows/upgrade-provider.yml`** — Updated action from `@v0.0.15` to `@v1`.

**`provider/go.mod`** — Removed `github.com/pulumi/pulumi-terraform-bridge/pf v0.49.0`
(the standalone `/pf` module was deleted upstream at bridge v3.97.0; the functionality moved
into the main `v3` module at `pkg/pf/tfbridge`). The `provider/resources.go` import already
uses the correct path `github.com/pulumi/pulumi-terraform-bridge/v3/pkg/pf/tfbridge`.

### To create the PR

```bash
git checkout claude/automate-provider-updates-2DiaM
# No further changes needed — everything is committed and pushed
# Create PR via GitHub MCP tools or gh CLI:
gh pr create \
  --base main \
  --title "ci: add lint, unit-test, schema-validation jobs; fix deprecated golangci linters" \
  --body "..."
```

---

## Phase 1 — Delete 14 Stale Branches

Can run any time, independent of other phases.

```bash
for branch in \
  upgrade-pulumi-terraform-bridge-to-v3.91.0-98836590 \
  upgrade-pulumi-terraform-bridge-to-v3.97.1-ci \
  upgrade-pulumi-terraform-bridge-to-v3.98.0-ci \
  upgrade-terraform-provider-fivetran-to-v1.3.3-78652080 \
  upgrade-terraform-provider-fivetran-to-v1.4.0-ci \
  upgrade-terraform-provider-fivetran-to-v1.4.0 \
  upgrade-terraform-provider-fivetran-to-v1.4.1-ci \
  upgrade-terraform-provider-fivetran-to-v1.4.2-ci \
  upgrade-terraform-provider-fivetran-to-v1.4.2 \
  upgrade-terraform-provider-fivetran-to-v1.5.0-ci \
  upgrade-terraform-provider-fivetran-to-v1.5.0 \
  upgrade-terraform-provider-fivetran-to-v1.5.1-ci \
  upgrade-terraform-provider-fivetran-to-v1.5.1 \
  upgrade-terraform-provider-fivetran-to-v1.9.4; do
  git push origin --delete "$branch"
done
```

---

## Phase 2 — Bridge Upgrade v3.111.0 → v3.126.0

**Blocked until Phase 0 PR is merged to main.**  
Branch: `upgrade-bridge-to-v3.126.0` from `main`.

### Pre-conditions confirmed during Phase 0

- `provider/resources.go` already uses correct import `v3/pkg/pf/tfbridge` ✅
- The standalone `/pf` require in `go.mod` is already removed ✅
- These changes are in the Phase 0 PR, so after merge the main branch will be clean

### Manual changes required (upgrade-provider CLI will NOT do these)

**a) `mise.toml`** — bump Go version (if present):
```toml
# before
go = "1.23"
# after
go = "1.25"
```

**b) `.github/workflows/pull-request.yml`** — bump Go in matrix:
```yaml
goversion:
  - 1.25.x   # was 1.23.x
```

**c) `provider/go.mod`** — bridge v3.111.0 → v3.126.0 requires Go 1.25:
```
go 1.25
toolchain go1.25.x
```

### Use upgrade-provider CLI for go.mod + regeneration

```bash
git checkout main && git pull origin main
git checkout -b upgrade-bridge-to-v3.126.0
mise install   # installs Go 1.25 and other tools

# Apply manual changes above first, then:
upgrade-provider ryan-pip/pulumi-fivetran \
  --kind=bridge \
  --target-bridge-version=v3.126.0
```

The CLI updates `provider/go.mod` (bridge v3.111.0→v3.126.0), runs `go mod tidy`,
runs `make generate`, commits, pushes.

### Validation checklist
1. `go build ./...` succeeds
2. `go vet ./...` passes
3. `golangci-lint` passes
4. `make schema` generates without error
5. Schema resource count > 0
6. Worktree-clean check passes (committed schema matches generated)
7. All SDK builds pass
8. Manual: compare `schema.json` before/after — bridge upgrade should produce minimal
   schema changes (formatting only, no resource additions/removals)

### What "broken" looks like
- Build fails → `/pf` import not fully migrated (grep: `grep -r "terraform-bridge/pf"`)
- `make schema` fails → bridge API incompatibility; check bridge CHANGELOG for breaking changes
- Schema has 0 resources → tfgen crashed silently; inspect stderr from schema generation
- SDK builds fail after schema succeeds → codegen template change in new bridge
- Lint fails → new bridge code exposed previously-hidden linting issues

---

## Phase 3 — Provider Upgrade v1.9.4 → v1.9.29

**Blocked until Phase 2 is merged to main.**  
Branch: `upgrade-provider-to-v1.9.29` from `main`.

```bash
git checkout main && git pull origin main
upgrade-provider ryan-pip/pulumi-fivetran \
  --kind=provider \
  --target-version=v1.9.29
```

The CLI updates `provider/go.mod` and `provider/shim/go.mod`
(fivetran v1.9.4→v1.9.29), runs `go mod tidy` in both, runs `make generate`,
commits, pushes, and creates PR.

### Manual fallback (if CLI fails or doesn't handle shim)

```bash
git checkout -b upgrade-provider-to-v1.9.29

cd provider/shim
go get github.com/fivetran/terraform-provider-fivetran@v1.9.29
go mod tidy

cd ../..
cd provider
go get github.com/fivetran/terraform-provider-fivetran@v1.9.29
go mod tidy

make generate
git add -A
git commit -m "Upgrade terraform-provider-fivetran to v1.9.29"
git push -u origin upgrade-provider-to-v1.9.29
```

### Validation for provider upgrade
- Schema WILL change (new resources/properties in v1.9.29 vs v1.9.4) — this is expected
- Review fivetran terraform-provider CHANGELOG from v1.9.4 to v1.9.29:
  - Any **removed resources** → existing users' stacks would fail on next `pulumi up`
  - Any **renamed resources** → may need aliases in `resources.go`
  - Any **type changes on required fields** → potential state corruption
- Schema resource count must be ≥ count from v1.9.4 (resources are rarely removed)

---

## Phase 4 — Ongoing Automation (self-maintaining after all PRs land)

After all three PRs merge:
1. Daily `upgrade-provider.yml` runs at 05:00 UTC
2. Detects new upstream versions and creates PRs automatically
3. Those PRs go through lint + vet + unit-test + schema-validation + build
4. If CI passes, review and merge; if CI fails, the failure is meaningful

No further changes required.

---

## Out of Scope

**Integration tests against real Fivetran API**: Requires `FIVETRAN_APIKEY` and
`FIVETRAN_APISECRET` secrets. The `examples/` directory has the framework but no test
programs. Add as a future PR once credentials are available in GitHub secrets.

---

## Key Files

| File | Phase | Change |
|---|---|---|
| `.golangci.yml` | 0 ✅ | Fixed 6 deprecated linters, golangci-lint v2 format |
| `.github/workflows/pull-request.yml` | 0 ✅ | Added lint/unit-test/schema-validation jobs |
| `.github/workflows/upgrade-provider.yml` | 0 ✅ | Updated action to `@v1` |
| `provider/go.mod` | 0 ✅ | Removed standalone `/pf` bridge require |
| `mise.toml` | 2 | Go 1.23 → 1.25 |
| `provider/go.mod` | 2 | Bridge v3.111.0 → v3.126.0, Go 1.25 |
| `provider/go.mod` + `provider/shim/go.mod` | 3 | Fivetran v1.9.4 → v1.9.29 |

## Execution Order

```
Phase 0 (repo uplift — branch ready, needs PR+merge)
Phase 1 (branch cleanup — can run any time)
     │
     ▼ (after Phase 0 lands on main)
Phase 2 (bridge upgrade v3.111.0 → v3.126.0)
     │
     ▼ (after Phase 2 lands on main)
Phase 3 (provider upgrade v1.9.4 → v1.9.29)
     │
     ▼
Phase 4 (ongoing automation — no action needed)
```
