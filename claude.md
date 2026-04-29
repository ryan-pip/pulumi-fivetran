# CLAUDE.md

`pulumi-fivetran` is a [Pulumi](https://www.pulumi.com/) resource provider for [Fivetran](https://www.fivetran.io/), bridged from the upstream Terraform provider [`fivetran/terraform-provider-fivetran`](https://github.com/fivetran/terraform-provider-fivetran) via [`pulumi-terraform-bridge`](https://github.com/pulumi/pulumi-terraform-bridge) v3.

## Architecture

```
upstream terraform-provider-fivetran (Go module)
            │
            ▼
provider/resources.go ─────► tfgen binary (bin/pulumi-tfgen-fivetran)
                                   │
                                   ▼
                       provider/cmd/pulumi-resource-fivetran/
                       ├── schema.json
                       ├── bridge-metadata.json
                       └── schema-embed.json
                                   │
              ┌────────────────────┼────────────────────┬──────────────────┐
              ▼                    ▼                    ▼                  ▼
        sdk/nodejs/           sdk/python/            sdk/go/         sdk/dotnet/
```

- [provider/](provider/) — Go module with bridge wiring ([provider/resources.go](provider/resources.go)) and two binaries: `tfgen` and `pulumi-resource-fivetran`.
- [sdk/](sdk/) — generated, checked in. See rule `generated-code`.
- [examples/](examples/) — independent Go module (not in [go.work](go.work)); used by Python integration tests via `GOWORK=off`.
- [tests/python/](tests/python/) — Pulumi mock-runtime smoke tests.
- `.make/` — sentinel files for incremental Makefile builds (gitignored). See rule `make-targets`.

## Common commands

```bash
make build                                                    # tfgen → schema → provider → all 4 SDKs
make schema                                                   # after editing provider/resources.go
make build_python                                             # one SDK (also build_nodejs|build_go|build_dotnet)
make lint
cd provider && go test -v -short -parallel 10 . ./pkg/...     # provider unit tests
make test_python_smoke                                        # mocked Python SDK
make test_python                                              # live integration (needs FIVETRAN_*)
```

## CI workflows

- [pull-request.yml](.github/workflows/pull-request.yml) — `lint`, `schema-validation`, `go-test`, single `prerequisites` build, then matrix `build_sdk` + `python_tests` consuming the prebuilt artifact.
- [release.yml](.github/workflows/release.yml) — `v*.*.*` tags. 6-shard goreleaser matrix, then per-language SDK publish. PyPI + npm via OIDC; NuGet gated by `PUBLISH_NUGET=false`.
- [upgrade-provider.yml](.github/workflows/upgrade-provider.yml) — daily cron; auto-merge gated by author + branch-prefix filters. See rule `auto-merge-safety`.
- [auto-tag.yml](.github/workflows/auto-tag.yml) — mirrors upstream `terraform-provider-fivetran` tags when `provider/go.mod` changes on `main`. Uses `RELEASE_BOT` GitHub App.

## Where to look

- Provider behavior: [provider/resources.go](provider/resources.go), [provider/pkg/](provider/pkg/)
- Toolchain: [mise.toml](mise.toml) (dev), [mise.ci.toml](mise.ci.toml) (CI subset — keep shared tools in sync). Pre-commit via `hk` ([hk.pkl](hk.pkl)).
- Project rules and skills: [.claude/rules/](.claude/rules/), [.claude/skills/](.claude/skills/)
- Upstream: `fivetran/terraform-provider-fivetran` GitHub; `pulumi-terraform-bridge` v3 docs
