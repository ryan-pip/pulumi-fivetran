## Context

`auto-tag.yml` and `upgrade-provider.yml` are siblings: both mint a token from this repo's release-bot GitHub App via `actions/create-github-app-token` (using `vars.RELEASE_BOT_APP_ID` / `secrets.RELEASE_BOT_PRIVATE_KEY`) and use it to push to the repo. `upgrade-provider.yml`'s `Set up git identity` step was de-hardcoded to derive the committer identity from the minting app:

```bash
NAME="${{ steps.app-token.outputs.app-slug }}[bot]"
ID=$(gh api "/users/${NAME}" --jq .id)
git config --global user.name "$NAME"
git config --global user.email "${ID}+${NAME}@users.noreply.github.com"
```

`auto-tag.yml`'s `Push tag` step was never updated and still runs:

```bash
git config user.name 'pulumi-release-bot[bot]'
git config user.email 'pulumi-release-bot[bot]@users.noreply.github.com'
```

The app behind `RELEASE_BOT_APP_ID` is this repo's own app, whose slug is not necessarily `pulumi-release-bot`, and the canonical noreply address for a GitHub App bot is `<numeric-id>+<slug>[bot]@users.noreply.github.com` — neither of which the hardcoded values match. (This repo's `auto-tag` triggers on `provider/shim/go.mod` bumps; the trigger is unrelated to the fix and stays as-is.)

## Goals / Non-Goals

**Goals:**
- Make `auto-tag.yml`'s tagger identity match the app that actually pushes the tag, so tags are correctly attributed and verified.
- Use the exact derivation already proven in `upgrade-provider.yml`, so the two workflows stay consistent.

**Non-Goals:**
- Changing when or whether tags are pushed (the trigger, version-gate, and existing-tag guard are unchanged).
- Touching `upgrade-provider.yml`, which already does this correctly.
- Signing tags (GPG/SSH) — out of scope; this only fixes the tagger identity.

## Decisions

**Derive the identity at run time from `app-slug`, matching `upgrade-provider.yml` verbatim.** The token is minted earlier in the same job (`id: app-token`), so `steps.app-token.outputs.app-slug` is available, and `gh api /users/<slug>[bot]` returns the bot user's numeric id. Reusing the identical snippet (rather than inventing a new mechanism) keeps the two workflows aligned and makes the spec's "same as upgrade-provider" requirement literally true.

- _Alternative — hardcode the correct slug/id once:_ rejected. It re-introduces the same brittleness we removed from `upgrade-provider.yml`; if the app is ever rotated or renamed, the value drifts silently.
- _Alternative — drop annotation, push a lightweight tag with no tagger:_ rejected. Annotated tags carry the `chore(release): ...` message used downstream; we only want to fix the identity, not change the tag object.

**Add `GH_TOKEN` to the `Push tag` step's `env`.** The step currently only sets `TAG`. The `gh api` lookup needs authentication; the minted app token is the natural choice and is already in scope.

## Risks / Trade-offs

- [The `gh api /users/<slug>[bot]` lookup fails or rate-limits] → With `GH_TOKEN` set to the app token the call is authenticated and the per-run cost is a single request; `upgrade-provider.yml` already relies on the identical call without issue.
- [`app-slug` output differs from expectation] → That is precisely the bug being fixed: the derived value is authoritative for whichever app `RELEASE_BOT_APP_ID` points at, so using it is correct by construction.

## Migration Plan

Single-commit workflow edit; no data or state migration. Takes effect on the next `auto-tag-upstream-bump` run (next upstream bump merged to `main`). Rollback is reverting the one commit. Prior tags are unaffected.

## Open Questions

None.
