# Plan: pulumi-fivetran

**Last updated**: 2026-04-30

## Status

The repo modernization tracking the [pulumi-astronomer template](../pulumi-astronomer)
has landed in four PRs:

| PR | Wave | Scope |
|---|---|---|
| #46 (merged) | 1 | Toolchain — mise.toml + mise.ci.toml + hk.pkl pre-commit, drop .go-version |
| #45 (merged) | 1 | AI — `claude.md` + `.claude/{settings,rules,skills}` |
| #47 (merged) | 2 | Build — Makefile rewrite, RespectSchemaVersion + PyProject in resources.go, SDK regen |
| #48 (open)   | 2 | CI — parallel pull-request/release pipelines, OIDC trusted publishing, mocked Python smoke tests, auto-tag.yml |

**Tag cleanup**: deleted v1.9.4 / v1.9.5 / v1.9.6 / v1.9.7 (releases that
never had passing CI) along with their orphaned draft GitHub releases.
Latest valid tag is `v1.5.1`.

## Outstanding

### Setup follow-ups (after PR #48 merges)
- **OIDC trusted publishing** — configure Trusted Publishers on
  [npmjs.com](https://docs.npmjs.com/trusted-publishers) for
  `@ryan-pip/pulumi-fivetran` and on
  [pypi.org](https://docs.pypi.org/trusted-publishers/) for
  `pulumi_provider_fivetran` before the next release tag is cut.
- **auto-tag.yml prereqs** — provision a `pulumi-release-bot` GitHub App,
  install on this repo, and set `vars.RELEASE_BOT_APP_ID` +
  `secrets.RELEASE_BOT_PRIVATE_KEY`. Without these, `auto-tag.yml` will
  fail to mint its app token.

### Provider upgrade v1.9.4 → latest
The new [upgrade-provider.yml](.github/workflows/upgrade-provider.yml)
runs daily at 05:00 UTC and will open `upgrade-terraform-provider-fivetran-*`
PRs automatically. Auto-merge fires when CI is green (gated on bot author +
branch-prefix safety filters). Manual fallback:

```bash
upgrade-provider ryan-pip/pulumi-fivetran --kind=provider --target-version=v1.9.X
```

### First post-modernization tag
Once the provider upgrade lands, decide on the new tag (e.g., `v2.0.0` to
signal the publish-pipeline change, or resume the `v1.9.X` line). Confirm
Trusted Publishers are configured first, then:

```bash
git pull --ff-only origin main
git log -1 --oneline   # confirm HEAD
git tag -a vX.Y.Z -m 'release vX.Y.Z'
git push origin vX.Y.Z
```

## Reference

- Project rules: [.claude/rules/](.claude/rules/)
- Repeatable SDK regen workflow: [.claude/skills/regenerate-sdks/SKILL.md](.claude/skills/regenerate-sdks/SKILL.md)
- Full migration plan (with rationale, file inventories, exact substitutions):
  `~/.claude/plans/i-started-getting-this-tranquil-sparkle.md`
