## 1. Fix the auto-tag git identity

- [x] 1.1 In `.github/workflows/auto-tag.yml`, add `GH_TOKEN: ${{ steps.app-token.outputs.token }}` to the `Push tag` step's `env` (alongside the existing `TAG`).
- [x] 1.2 In the `Push tag` step's run script, replace the two hardcoded `git config` lines with the dynamic derivation used by `upgrade-provider.yml`: set `NAME="${{ steps.app-token.outputs.app-slug }}[bot]"`, `ID=$(gh api "/users/${NAME}" --jq .id)`, then `git config user.name "$NAME"` and `git config user.email "${ID}+${NAME}@users.noreply.github.com"`.
- [x] 1.3 Add a brief comment above the identity block (mirroring `upgrade-provider.yml`) explaining it uses this repo's own release-bot app identity, not the hardcoded upstream `pulumi-release-bot`.

## 2. Verify

- [x] 2.1 Confirm the `Push tag` step's identity derivation matches `upgrade-provider.yml`'s `Set up git identity` step (same `app-slug`/`gh api`/email format), so the two workflows are consistent.
- [x] 2.2 Lint the workflow (`actionlint .github/workflows/auto-tag.yml`) and confirm no YAML/shell issues.
- [x] 2.3 Sanity-check the rest of the `Push tag` step is unchanged: same trigger (`provider/shim/go.mod`), version-gate, existing-tag guard, and annotated `git tag -a ... -m "chore(release): ..."` message.
