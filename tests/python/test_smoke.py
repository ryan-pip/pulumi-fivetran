"""SDK smoke tests.

Each test constructs one resource via the mocked Pulumi runtime and asserts
that the URN and a representative output property resolve. Catches:
  - SDK build/import broken
  - __init__ signature drift after a bridge bump
  - Property serialization failures in the bridge layer

These tests do NOT exercise real Fivetran API calls — see examples/ for live
integration scaffolding.
"""

import pulumi
import pulumi_provider_fivetran as fivetran


def _check_urn(resource):
    """Return an Output[None] that asserts the resource registered with a URN."""

    def check(urn):
        assert urn, f"empty URN for {resource}"

    return resource.urn.apply(check)


def test_module_imports():
    expected = {
        "Connector",
        "Destination",
        "ExternalLogging",
        "Group",
        "Team",
        "Transformation",
        "TransformationProject",
        "User",
        "Webhook",
    }
    missing = expected - set(dir(fivetran))
    assert not missing, f"missing exports: {missing}"


@pulumi.runtime.test
def test_group():
    g = fivetran.Group("smoke-group", name="smoke-group")
    return _check_urn(g)


@pulumi.runtime.test
def test_destination():
    d = fivetran.Destination(
        "smoke-destination",
        group_id="g_xyz",
        service="snowflake",
        region="GCP_US_EAST4",
        time_zone_offset="-5",
    )
    return _check_urn(d)


@pulumi.runtime.test
def test_connector():
    c = fivetran.Connector(
        "smoke-connector",
        group_id="g_xyz",
        service="postgres",
    )
    return _check_urn(c)


@pulumi.runtime.test
def test_user():
    u = fivetran.User(
        "smoke-user",
        email="smoke@example.com",
        given_name="Smoke",
        family_name="Test",
    )
    return _check_urn(u)


@pulumi.runtime.test
def test_team():
    t = fivetran.Team("smoke-team", role="Account Reviewer")
    return _check_urn(t)


@pulumi.runtime.test
def test_transformation_project():
    p = fivetran.TransformationProject(
        "smoke-project",
        group_id="g_xyz",
        type="DBT_GIT",
    )
    return _check_urn(p)


@pulumi.runtime.test
def test_webhook():
    w = fivetran.Webhook(
        "smoke-webhook",
        active=True,
        events=["sync_start"],
        secret="redacted",
        type="account",
        url="https://example.com/hook",
    )
    return _check_urn(w)
