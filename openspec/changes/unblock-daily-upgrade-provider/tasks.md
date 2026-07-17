# Tasks — unblock-daily-upgrade-provider (fivetran)

## 1. Go toolchain fix

- [x] 1.1 In `mise.toml` `[env]`, change `GOTOOLCHAIN = "go1.25.9"` to `GOTOOLCHAIN = "auto"` with a one-line comment stating why an exact pin is forbidden (drift vs `mise.lock` broke the daily upgrade)
- [x] 1.2 Verify locally: `cd provider && go get github.com/pulumi/pulumi-terraform-bridge/v3@v3.134.0 && go mod tidy` succeeds and bumps the `go` directive to 1.25.11 (revert after verifying — the bot owns bridge bumps)

## 2. PR + automation verification

- [x] 2.1 Open the one-line PR (branch + Jira ref per repo conventions); confirm `pull-request.yml` is green
- [ ] 2.2 After merge, confirm the next scheduled `upgrade-provider` run completes and opens the bridge v3.134.0 upgrade PR: `gh run list --workflow upgrade-provider.yml --limit 1`
- [ ] 2.3 Confirm the bot PR auto-merges per the auto-merge safety filters (bot author + `upgrade-*` branch prefix) and its CI is green under the new toolchain setting
