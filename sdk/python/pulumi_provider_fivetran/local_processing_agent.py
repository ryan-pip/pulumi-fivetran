# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['LocalProcessingAgentArgs', 'LocalProcessingAgent']

@pulumi.input_type
class LocalProcessingAgentArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 group_id: pulumi.Input[str],
                 authentication_counter: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a LocalProcessingAgent resource.
        :param pulumi.Input[str] display_name: The unique name for the local processing agent.
        :param pulumi.Input[str] group_id: The unique identifier for the Group within the Fivetran system.
        :param pulumi.Input[int] authentication_counter: Determines whether re-authentication needs to be performed.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "group_id", group_id)
        if authentication_counter is not None:
            pulumi.set(__self__, "authentication_counter", authentication_counter)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The unique name for the local processing agent.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The unique identifier for the Group within the Fivetran system.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="authenticationCounter")
    def authentication_counter(self) -> Optional[pulumi.Input[int]]:
        """
        Determines whether re-authentication needs to be performed.
        """
        return pulumi.get(self, "authentication_counter")

    @authentication_counter.setter
    def authentication_counter(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "authentication_counter", value)


@pulumi.input_type
class _LocalProcessingAgentState:
    def __init__(__self__, *,
                 auth_json: Optional[pulumi.Input[str]] = None,
                 authentication_counter: Optional[pulumi.Input[int]] = None,
                 config_json: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 docker_compose_yaml: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 registered_at: Optional[pulumi.Input[str]] = None,
                 usages: Optional[pulumi.Input[Sequence[pulumi.Input['LocalProcessingAgentUsageArgs']]]] = None):
        """
        Input properties used for looking up and filtering LocalProcessingAgent resources.
        :param pulumi.Input[str] auth_json: Base64-encoded content of the auth.json file.
        :param pulumi.Input[int] authentication_counter: Determines whether re-authentication needs to be performed.
        :param pulumi.Input[str] config_json: Base64-encoded content of the config.json file.
        :param pulumi.Input[str] display_name: The unique name for the local processing agent.
        :param pulumi.Input[str] docker_compose_yaml: Base64-encoded content of the compose file for the chosen containerization type.
        :param pulumi.Input[str] group_id: The unique identifier for the Group within the Fivetran system.
        :param pulumi.Input[str] registered_at: The timestamp of the time the local processing agent was created in your account.
        """
        if auth_json is not None:
            pulumi.set(__self__, "auth_json", auth_json)
        if authentication_counter is not None:
            pulumi.set(__self__, "authentication_counter", authentication_counter)
        if config_json is not None:
            pulumi.set(__self__, "config_json", config_json)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if docker_compose_yaml is not None:
            pulumi.set(__self__, "docker_compose_yaml", docker_compose_yaml)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if registered_at is not None:
            pulumi.set(__self__, "registered_at", registered_at)
        if usages is not None:
            pulumi.set(__self__, "usages", usages)

    @property
    @pulumi.getter(name="authJson")
    def auth_json(self) -> Optional[pulumi.Input[str]]:
        """
        Base64-encoded content of the auth.json file.
        """
        return pulumi.get(self, "auth_json")

    @auth_json.setter
    def auth_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_json", value)

    @property
    @pulumi.getter(name="authenticationCounter")
    def authentication_counter(self) -> Optional[pulumi.Input[int]]:
        """
        Determines whether re-authentication needs to be performed.
        """
        return pulumi.get(self, "authentication_counter")

    @authentication_counter.setter
    def authentication_counter(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "authentication_counter", value)

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> Optional[pulumi.Input[str]]:
        """
        Base64-encoded content of the config.json file.
        """
        return pulumi.get(self, "config_json")

    @config_json.setter
    def config_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_json", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique name for the local processing agent.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="dockerComposeYaml")
    def docker_compose_yaml(self) -> Optional[pulumi.Input[str]]:
        """
        Base64-encoded content of the compose file for the chosen containerization type.
        """
        return pulumi.get(self, "docker_compose_yaml")

    @docker_compose_yaml.setter
    def docker_compose_yaml(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "docker_compose_yaml", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier for the Group within the Fivetran system.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="registeredAt")
    def registered_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of the time the local processing agent was created in your account.
        """
        return pulumi.get(self, "registered_at")

    @registered_at.setter
    def registered_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registered_at", value)

    @property
    @pulumi.getter
    def usages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LocalProcessingAgentUsageArgs']]]]:
        return pulumi.get(self, "usages")

    @usages.setter
    def usages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LocalProcessingAgentUsageArgs']]]]):
        pulumi.set(self, "usages", value)


class LocalProcessingAgent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_counter: Optional[pulumi.Input[int]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        NOTE: In connection with the general availability of the hybrid deployment functionality and in order to synchronize internal terminology, we have deprecate this resource.

        This resource allows you to create, update, and delete local processing agents.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_provider_fivetran as fivetran

        test_lpa = fivetran.LocalProcessingAgent("testLpa",
            display_name="display_name",
            group_id="group_id",
            opts = pulumi.ResourceOptions(provider=fivetran_provider))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] authentication_counter: Determines whether re-authentication needs to be performed.
        :param pulumi.Input[str] display_name: The unique name for the local processing agent.
        :param pulumi.Input[str] group_id: The unique identifier for the Group within the Fivetran system.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocalProcessingAgentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NOTE: In connection with the general availability of the hybrid deployment functionality and in order to synchronize internal terminology, we have deprecate this resource.

        This resource allows you to create, update, and delete local processing agents.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_provider_fivetran as fivetran

        test_lpa = fivetran.LocalProcessingAgent("testLpa",
            display_name="display_name",
            group_id="group_id",
            opts = pulumi.ResourceOptions(provider=fivetran_provider))
        ```

        :param str resource_name: The name of the resource.
        :param LocalProcessingAgentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocalProcessingAgentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_counter: Optional[pulumi.Input[int]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocalProcessingAgentArgs.__new__(LocalProcessingAgentArgs)

            __props__.__dict__["authentication_counter"] = authentication_counter
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["auth_json"] = None
            __props__.__dict__["config_json"] = None
            __props__.__dict__["docker_compose_yaml"] = None
            __props__.__dict__["registered_at"] = None
            __props__.__dict__["usages"] = None
        super(LocalProcessingAgent, __self__).__init__(
            'fivetran:index/localProcessingAgent:LocalProcessingAgent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth_json: Optional[pulumi.Input[str]] = None,
            authentication_counter: Optional[pulumi.Input[int]] = None,
            config_json: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            docker_compose_yaml: Optional[pulumi.Input[str]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            registered_at: Optional[pulumi.Input[str]] = None,
            usages: Optional[pulumi.Input[Sequence[pulumi.Input[Union['LocalProcessingAgentUsageArgs', 'LocalProcessingAgentUsageArgsDict']]]]] = None) -> 'LocalProcessingAgent':
        """
        Get an existing LocalProcessingAgent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_json: Base64-encoded content of the auth.json file.
        :param pulumi.Input[int] authentication_counter: Determines whether re-authentication needs to be performed.
        :param pulumi.Input[str] config_json: Base64-encoded content of the config.json file.
        :param pulumi.Input[str] display_name: The unique name for the local processing agent.
        :param pulumi.Input[str] docker_compose_yaml: Base64-encoded content of the compose file for the chosen containerization type.
        :param pulumi.Input[str] group_id: The unique identifier for the Group within the Fivetran system.
        :param pulumi.Input[str] registered_at: The timestamp of the time the local processing agent was created in your account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LocalProcessingAgentState.__new__(_LocalProcessingAgentState)

        __props__.__dict__["auth_json"] = auth_json
        __props__.__dict__["authentication_counter"] = authentication_counter
        __props__.__dict__["config_json"] = config_json
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["docker_compose_yaml"] = docker_compose_yaml
        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["registered_at"] = registered_at
        __props__.__dict__["usages"] = usages
        return LocalProcessingAgent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authJson")
    def auth_json(self) -> pulumi.Output[str]:
        """
        Base64-encoded content of the auth.json file.
        """
        return pulumi.get(self, "auth_json")

    @property
    @pulumi.getter(name="authenticationCounter")
    def authentication_counter(self) -> pulumi.Output[int]:
        """
        Determines whether re-authentication needs to be performed.
        """
        return pulumi.get(self, "authentication_counter")

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> pulumi.Output[str]:
        """
        Base64-encoded content of the config.json file.
        """
        return pulumi.get(self, "config_json")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The unique name for the local processing agent.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dockerComposeYaml")
    def docker_compose_yaml(self) -> pulumi.Output[str]:
        """
        Base64-encoded content of the compose file for the chosen containerization type.
        """
        return pulumi.get(self, "docker_compose_yaml")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The unique identifier for the Group within the Fivetran system.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="registeredAt")
    def registered_at(self) -> pulumi.Output[str]:
        """
        The timestamp of the time the local processing agent was created in your account.
        """
        return pulumi.get(self, "registered_at")

    @property
    @pulumi.getter
    def usages(self) -> pulumi.Output[Sequence['outputs.LocalProcessingAgentUsage']]:
        return pulumi.get(self, "usages")

