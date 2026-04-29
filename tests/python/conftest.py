"""Pulumi mock runtime for SDK smoke tests.

Set up before any pulumi_provider_fivetran import so resource registrations
go through MockRuntime instead of trying to talk to a real engine.
"""

import pulumi


class _FivetranMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        # Echo inputs back as outputs; assign a deterministic ID derived from name.
        return [args.name + "_id", args.inputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}


pulumi.runtime.set_mocks(_FivetranMocks(), preview=False)
