---
description: Generated code in sdk/ and provider/cmd/pulumi-resource-fivetran/*.json must never be hand-edited — always regenerate via tfgen.
paths:
  - "sdk/**"
  - "provider/cmd/pulumi-resource-fivetran/schema.json"
  - "provider/cmd/pulumi-resource-fivetran/bridge-metadata.json"
  - "provider/cmd/pulumi-resource-fivetran/schema-embed.json"
  - "hk.pkl"
---

# Generated Code: Don't Hand-Edit

These paths are codegenned and checked in. Always regenerate, never edit by hand:

- `provider/cmd/pulumi-resource-fivetran/schema.json`
- `provider/cmd/pulumi-resource-fivetran/bridge-metadata.json`
- `provider/cmd/pulumi-resource-fivetran/schema-embed.json`
- All of `sdk/nodejs/`, `sdk/python/`, `sdk/go/`, `sdk/dotnet/`

## Regeneration

After editing `provider/resources.go` or bumping the bridge / upstream provider:

```bash
make schema build_sdks
```

If diffs look unrelated to your change, run `cd provider && go mod tidy` and retry.

See the `regenerate-sdks` skill for the full ordered flow.

## CI enforcement

`pull-request.yml` runs `make build_$lang` and then verifies a clean worktree, with a small allowlist for version-bearing files:

```
sdk/.*/pulumi-plugin\.json
sdk/nodejs/package\.json
sdk/python/pyproject\.toml
sdk/go/.*/internal/pulumiUtilities\.go
```

Anything else dirty after an SDK build = the job fails. Hand edits get caught here.

## hk excludes

`hk.pkl` excludes these paths from formatters/linters. Don't extend hk to "fix" generated code — just regenerate. If the generated output is wrong, fix it upstream (in `provider/resources.go`, the bridge, or the TF provider) and re-tfgen.
