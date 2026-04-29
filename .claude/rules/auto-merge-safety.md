---
description: Auto-merge in upgrade-provider.yml requires BOTH the github-actions[bot] author filter AND the upgrade-* branch prefix regex. Don't loosen either.
paths:
  - ".github/workflows/upgrade-provider.yml"
  - ".github/workflows/auto-tag.yml"
---

# Auto-Merge Safety

`upgrade-provider.yml` enables auto-merge **only** when both filters pass:

1. `--author 'app/github-actions'` — bot identity (the action's identity when `GH_TOKEN=GITHUB_TOKEN`).
2. Branch name matches `^upgrade-(pulumi-terraform-bridge|terraform-provider|pulumi-version)-`.

Together they prevent auto-merging a human PR even if:

- A human commits to a coincidentally-named `upgrade-*` branch (the author check stops that).
- The bot opens a PR on a non-upgrade branch (the prefix check stops that).

## Don't

- **Don't** loosen the author filter to `--author '*[bot]'` — third-party bots (Renovate, semantic-release, etc.) can match and slip through.
- **Don't** drop the branch prefix check. Each upgrade type from `pulumi-upgrade-provider-action` controls its own branch name; new template categories require an explicit prefix entry here.
- **Don't** add auto-merge to non-upgrade flows in this same workflow. Auto-merge for human PRs is a separate decision and should be opt-in per PR via `gh pr merge --auto` by the author.
- **Don't** use `--admin` on `gh pr merge` — bypassing required reviews defeats the safety net.

## When adding a new upgrade type

If a new bumper opens PRs with a different branch prefix (e.g. `upgrade-go-toolchain-*`), add the prefix to the regex **and** verify the new bumper actually authors as `app/github-actions`. If it uses a different bot identity, the author filter needs widening too — and that's a load-bearing decision; flag it for review rather than silently expanding it.
