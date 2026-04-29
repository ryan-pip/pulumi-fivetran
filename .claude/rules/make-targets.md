---
description: Makefile uses file targets and .make/ sentinels for incremental builds — CI relies on `make --touch` to skip already-built artifacts. Don't replace with .PHONY shortcuts or helper scripts.
paths:
  - "Makefile"
  - ".github/workflows/**"
  - ".github/actions/**"
---

# Make Targets: File Targets + Sentinels

The Makefile is the single entry point for build/test orchestration. It uses **file targets** and **sentinel files** in `.make/` (gitignored) to skip work that's already done.

## Pattern

```make
schema: .make/schema
.make/schema: bin/$(TFGEN)
	$(WORKING_DIR)/bin/$(TFGEN) schema --out provider/cmd/$(PROVIDER)
	cd provider && VERSION=$(PROVIDER_VERSION) go generate cmd/$(PROVIDER)/main.go
	@touch $@
```

Each SDK depends only on `.make/schema` (not on the provider binary), so all four SDKs can build in parallel after a single schema generation.

## CI exploits this

CI uploads the prebuilt `bin/` and `.make/` from a single `prerequisites` job, then dependent jobs download and run:

```bash
make --touch schema provider           # marks them as up-to-date
make build_python                      # only the SDK rebuilds
```

If you replace `.make/` sentinels with `.PHONY:` shortcuts, you'll force every CI shard to rebuild the provider.

## Adding a target

- Multi-step orchestration → Makefile recipe with `&& \` continuations (the existing pattern in `build_python`, `build_nodejs`, etc.).
- Generated outputs → declare them as file/sentinel targets, not `.PHONY`. This is what makes `make --touch` work in CI.
- A Python `conftest.py`, `pyproject.toml`, etc. configuring the test framework itself is fine — those are framework-native artifacts, not orchestration.
