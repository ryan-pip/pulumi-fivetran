## Why

`auto-tag.yml`'s `Push tag` step hardcodes the upstream `pulumi-release-bot[bot]` git identity, even though the token it pushes with is minted from **this repo's own** release-bot GitHub App (`vars.RELEASE_BOT_APP_ID`). The sibling `upgrade-provider.yml` was deliberately de-hardcoded to derive its committer identity from the app that mints the token (`steps.app-token.outputs.app-slug` + the app user's id), and the `ci-cd-pipelines` spec already requires that. `auto-tag.yml` was left behind, so every mirror tag it pushes is annotated with a fabricated tagger — a bare `pulumi-release-bot[bot]@users.noreply.github.com` with no numeric app id, for an app whose real slug is whatever this repo's `RELEASE_BOT_APP_ID` resolves to. The tag push still succeeds, but the tagger is misattributed and unverified, and it silently contradicts the identity used everywhere else in the same workflow family.

## What Changes

- Replace the two hardcoded `git config` lines in `auto-tag.yml`'s `Push tag` step with the same dynamic derivation `upgrade-provider.yml` uses: `NAME="${{ steps.app-token.outputs.app-slug }}[bot]"`, `ID=$(gh api "/users/${NAME}" --jq .id)`, then `git config user.name "$NAME"` and `git config user.email "${ID}+${NAME}@users.noreply.github.com"`.
- The `Push tag` step gains `GH_TOKEN: ${{ steps.app-token.outputs.token }}` in its `env` so the `gh api` lookup is authenticated (the app token is already minted earlier in the job).
- Extend the `ci-cd-pipelines` capability with a requirement that `auto-tag.yml` (like `upgrade-provider.yml`) attribute its tags to this repo's own bot identity and never hardcode the upstream `pulumi-release-bot` identity.

## Capabilities

### New Capabilities
<!-- none -->

### Modified Capabilities
- `ci-cd-pipelines`: add a requirement that the `auto-tag-upstream-bump` workflow attribute mirror tags to this repo's own release-bot identity, derived from the token-minting app's `app-slug`, rather than the hardcoded upstream `pulumi-release-bot` identity.

## Impact

- Modified: `.github/workflows/auto-tag.yml` (the `Push tag` step only).
- CI/release tooling only — no provider runtime or SDK behavior change. Tags are still pushed on the same trigger (`provider/shim/go.mod` bumps); only the tagger identity becomes correct and verified.
- Part of the two-repo effort to keep `pulumi-astronomer` and `pulumi-fivetran` on the same bot-identity pattern; each carries its own repo-local change.
