SHELL            := /bin/bash
PROJECT          := github.com/ryan-pip/pulumi-fivetran
PROVIDER_PATH    := provider
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version
TFGEN            := pulumi-tfgen-fivetran
PROVIDER         := pulumi-resource-fivetran
TESTPARALLELISM  := 4
WORKING_DIR      := $(shell pwd)

# Override in CI: `make [target] PROVIDER_VERSION=x.y.z` or set the env var.
# Local builds use this fixed default; CI sets it from `pulumictl get version`.
PROVIDER_VERSION ?= 1.0.0-alpha.0+dev

LDFLAGS := -X $(PROJECT)/$(VERSION_PATH)=$(PROVIDER_VERSION)

# Create sentinel and bin directories up front so `touch` targets don't fail.
_ := $(shell mkdir -p .make bin)

.PHONY: build development only_build schema provider build_sdks \
        build_nodejs build_python build_go build_dotnet \
        prepare_local_workspace test_python_smoke test_python \
        lint tidy fmt clean install_sdks install_nodejs_sdk \
        install_python_sdk install_go_sdk install_dotnet_sdk \
        sync-go-work

# ── top-level aliases ─────────────────────────────────────────────────────────

build: schema provider build_sdks

development: build install_sdks

only_build: build

# ── tfgen binary ──────────────────────────────────────────────────────────────

# File target: rebuilt only when provider source or go.mod/go.sum change.
bin/$(TFGEN): provider/resources.go provider/go.*
	cd provider && go build -o $(WORKING_DIR)/bin/$(TFGEN) \
		-ldflags "$(LDFLAGS)" $(PROJECT)/$(PROVIDER_PATH)/cmd/$(TFGEN)

# ── schema ────────────────────────────────────────────────────────────────────

# Sentinel: rebuilt only when tfgen binary is newer.
schema: .make/schema

# upstream upgrade-provider calls this
tfgen: schema

.make/schema: bin/$(TFGEN)
	$(WORKING_DIR)/bin/$(TFGEN) schema --out provider/cmd/$(PROVIDER)
	cd provider && VERSION=$(PROVIDER_VERSION) go generate cmd/$(PROVIDER)/main.go
	@touch $@

# ── provider binary ───────────────────────────────────────────────────────────

# File target: rebuilt only when schema changes.
provider: bin/$(PROVIDER)

bin/$(PROVIDER): .make/schema
	cd provider && go build -o $(WORKING_DIR)/bin/$(PROVIDER) \
		-ldflags "$(LDFLAGS)" $(PROJECT)/$(PROVIDER_PATH)/cmd/$(PROVIDER)

# ── CI workspace prep ─────────────────────────────────────────────────────────

# Builds everything CI needs before SDK jobs: tfgen, schema, provider binary.
# SDK jobs download the output of this target and run make --touch to skip it.
prepare_local_workspace: bin/$(TFGEN) .make/schema bin/$(PROVIDER)

# ── SDK targets ───────────────────────────────────────────────────────────────

# Each SDK depends only on the schema sentinel, not on the provider binary.
# This lets CI build all SDKs in parallel after downloading the prerequisites.

build_sdks: build_nodejs build_python build_go build_dotnet

# upstream upgrade-provider calls this
generate_sdks: build_sdks

build_nodejs: .make/build_nodejs

.make/build_nodejs: .make/schema
	$(WORKING_DIR)/bin/$(TFGEN) nodejs --out sdk/nodejs/
	cd sdk/nodejs/ && \
		yarn install && \
		yarn run tsc && \
		cp ../../README.md ../../LICENSE package.json yarn.lock ./bin/
	@touch $@

build_python: .make/build_python

.make/build_python: .make/schema
	$(WORKING_DIR)/bin/$(TFGEN) python --out sdk/python/
	cd sdk/python/ && \
		cp ../../README.md . && \
		rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
		cd ./bin && uv build --quiet --wheel
	@touch $@

build_go: .make/build_go

.make/build_go: .make/schema
	$(WORKING_DIR)/bin/$(TFGEN) go --out sdk/go/
	cd sdk/go/ && go mod tidy
	@touch $@

build_dotnet: .make/build_dotnet

.make/build_dotnet: .make/schema
	$(WORKING_DIR)/bin/$(TFGEN) dotnet --out sdk/dotnet/
	cd sdk/dotnet/ && \
		echo "$(PROVIDER_VERSION)" > version.txt && \
		dotnet build /p:Version=$(PROVIDER_VERSION)
	@touch $@

# ── install SDKs ──────────────────────────────────────────────────────────────

install_sdks: install_nodejs_sdk install_python_sdk install_go_sdk

install_nodejs_sdk:
	yarn link --cwd $(WORKING_DIR)/sdk/nodejs/bin

install_python_sdk:

install_go_sdk:

install_dotnet_sdk:
	mkdir -p $(WORKING_DIR)/nuget
	find . -name '*.nupkg' -print -exec cp -p {} ${WORKING_DIR}/nuget \;

# ── tests ─────────────────────────────────────────────────────────────────────

# Mocked Python SDK smoke tests — never touches system Python.
test_python_smoke: build_python
	cd tests/python && \
		uv venv --clear --quiet .venv && \
		. .venv/bin/activate && \
		uv pip install --quiet pytest "pulumi>=3.0.0,<4.0.0" && \
		uv pip install --quiet ../../sdk/python/bin/dist/pulumi_provider_fivetran-*.whl && \
		pytest -v

# Live Python integration tests against the Fivetran API.
# Requires FIVETRAN_APIKEY + FIVETRAN_APISECRET; tests skip when unset.
# GOWORK=off: examples/ is an independent module not in go.work.
# PATH prepend: makes the locally-built provider binary discoverable by the
# test's pulumi engine without downloading from GitHub Releases.
test_python: export PATH := $(WORKING_DIR)/bin:$(PATH)
test_python: provider build_python
	cd examples && GOWORK=off go test -v -tags=python -parallel 1 -timeout 30m -run 'TestAcc.*Py'

# ── lint / fmt / tidy ─────────────────────────────────────────────────────────

lint:
	cd provider && golangci-lint run --path-prefix provider -c ../.golangci.yml . ./pkg/...

tidy:
	find ./provider -name go.mod -execdir go mod tidy \;

# Aligns go.work's `go` directive with the highest `go` directive among the
# workspace modules. Run after bumping pulumi-terraform-bridge (which can pull
# a new minimum Go) so `go vet`, `golangci-lint`, and the provider build
# don't fail with "go.work lists go X.Y.Z".
sync-go-work:
	@MAX=$$(awk '/^go [0-9]/ {print $$2}' provider/go.mod provider/shim/go.mod sdk/go.mod | sort -V | tail -1); \
	 CURRENT=$$(awk '/^go [0-9]/ {print $$2; exit}' go.work); \
	 if [ "$$MAX" != "$$CURRENT" ]; then \
	   echo "Updating go.work go directive: $$CURRENT -> $$MAX"; \
	   go work edit -go="$$MAX"; \
	 else \
	   echo "go.work already at $$MAX"; \
	 fi

fmt:
	find . -name '*.go' | grep -v vendor | xargs gofmt -s -w

# ── clean ─────────────────────────────────────────────────────────────────────

clean:
	rm -rf sdk/{dotnet,nodejs,go,python}
	rm -rf bin/* .make/*

help:
	@grep -E '^[a-zA-Z_-]+:.*?##' Makefile | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'
