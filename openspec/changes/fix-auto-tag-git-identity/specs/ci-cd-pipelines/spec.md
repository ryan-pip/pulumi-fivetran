## ADDED Requirements

### Requirement: Auto-tag uses this repo's own bot identity

`auto-tag.yml` (the `auto-tag-upstream-bump` workflow) SHALL attribute the mirror tags it pushes to this repo's release-bot GitHub App identity — the app that mints the token via `actions/create-github-app-token` — derived dynamically from that step's `app-slug` output, and SHALL NOT hardcode the upstream `pulumi-release-bot` identity. The `Push tag` step SHALL set `user.name = "<app-slug>[bot]"` with the matching noreply `user.email` of the form `<bot-user-id>+<app-slug>[bot]@users.noreply.github.com`, where `<bot-user-id>` is resolved from the GitHub API for that bot user. The step SHALL pass the minted app token as `GH_TOKEN` so the API lookup is authenticated. This mirrors the identity derivation already required of `upgrade-provider.yml`.

#### Scenario: tags are attributed to this repo's bot

- **WHEN** the `auto-tag-upstream-bump` workflow configures git identity before pushing a mirror tag
- **THEN** `user.name` is `<app-slug>[bot]` for this repo's app and `user.email` is the matching `<bot-user-id>+<app-slug>[bot]@users.noreply.github.com`, not `pulumi-release-bot[bot]`

#### Scenario: the bot-user-id lookup is authenticated

- **WHEN** the `Push tag` step resolves the bot user's id via `gh api`
- **THEN** the step has `GH_TOKEN` set to the minted app token so the lookup succeeds
