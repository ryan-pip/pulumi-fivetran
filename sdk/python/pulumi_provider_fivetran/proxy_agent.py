# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProxyAgentArgs', 'ProxyAgent']

@pulumi.input_type
class ProxyAgentArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 group_region: pulumi.Input[str]):
        """
        The set of arguments for constructing a ProxyAgent resource.
        :param pulumi.Input[str] display_name: Proxy agent name.
        :param pulumi.Input[str] group_region: Data processing location. This is where Fivetran will operate and run computation on data.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "group_region", group_region)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Proxy agent name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="groupRegion")
    def group_region(self) -> pulumi.Input[str]:
        """
        Data processing location. This is where Fivetran will operate and run computation on data.
        """
        return pulumi.get(self, "group_region")

    @group_region.setter
    def group_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_region", value)


@pulumi.input_type
class _ProxyAgentState:
    def __init__(__self__, *,
                 created_by: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 group_region: Optional[pulumi.Input[str]] = None,
                 proxy_server_uri: Optional[pulumi.Input[str]] = None,
                 registred_at: Optional[pulumi.Input[str]] = None,
                 salt: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProxyAgent resources.
        :param pulumi.Input[str] created_by: The actor who created the proxy agent.
        :param pulumi.Input[str] display_name: Proxy agent name.
        :param pulumi.Input[str] group_region: Data processing location. This is where Fivetran will operate and run computation on data.
        :param pulumi.Input[str] proxy_server_uri: The proxy server URI.
        :param pulumi.Input[str] registred_at: The timestamp of the time the proxy agent was created in your account.
        :param pulumi.Input[str] salt: The salt.
        :param pulumi.Input[str] token: The auth token.
        """
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if group_region is not None:
            pulumi.set(__self__, "group_region", group_region)
        if proxy_server_uri is not None:
            pulumi.set(__self__, "proxy_server_uri", proxy_server_uri)
        if registred_at is not None:
            pulumi.set(__self__, "registred_at", registred_at)
        if salt is not None:
            pulumi.set(__self__, "salt", salt)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The actor who created the proxy agent.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Proxy agent name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="groupRegion")
    def group_region(self) -> Optional[pulumi.Input[str]]:
        """
        Data processing location. This is where Fivetran will operate and run computation on data.
        """
        return pulumi.get(self, "group_region")

    @group_region.setter
    def group_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_region", value)

    @property
    @pulumi.getter(name="proxyServerUri")
    def proxy_server_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The proxy server URI.
        """
        return pulumi.get(self, "proxy_server_uri")

    @proxy_server_uri.setter
    def proxy_server_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_server_uri", value)

    @property
    @pulumi.getter(name="registredAt")
    def registred_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of the time the proxy agent was created in your account.
        """
        return pulumi.get(self, "registred_at")

    @registred_at.setter
    def registred_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registred_at", value)

    @property
    @pulumi.getter
    def salt(self) -> Optional[pulumi.Input[str]]:
        """
        The salt.
        """
        return pulumi.get(self, "salt")

    @salt.setter
    def salt(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "salt", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The auth token.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


class ProxyAgent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 group_region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to create, update, and delete proxy agent.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_provider_fivetran as fivetran

        test_proxy_agent = fivetran.ProxyAgent("testProxyAgent",
            display_name="display_name",
            group_region="group_region",
            opts = pulumi.ResourceOptions(provider=fivetran_provider))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Proxy agent name.
        :param pulumi.Input[str] group_region: Data processing location. This is where Fivetran will operate and run computation on data.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProxyAgentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to create, update, and delete proxy agent.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_provider_fivetran as fivetran

        test_proxy_agent = fivetran.ProxyAgent("testProxyAgent",
            display_name="display_name",
            group_region="group_region",
            opts = pulumi.ResourceOptions(provider=fivetran_provider))
        ```

        :param str resource_name: The name of the resource.
        :param ProxyAgentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProxyAgentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 group_region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProxyAgentArgs.__new__(ProxyAgentArgs)

            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if group_region is None and not opts.urn:
                raise TypeError("Missing required property 'group_region'")
            __props__.__dict__["group_region"] = group_region
            __props__.__dict__["created_by"] = None
            __props__.__dict__["proxy_server_uri"] = None
            __props__.__dict__["registred_at"] = None
            __props__.__dict__["salt"] = None
            __props__.__dict__["token"] = None
        super(ProxyAgent, __self__).__init__(
            'fivetran:index/proxyAgent:ProxyAgent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            group_region: Optional[pulumi.Input[str]] = None,
            proxy_server_uri: Optional[pulumi.Input[str]] = None,
            registred_at: Optional[pulumi.Input[str]] = None,
            salt: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None) -> 'ProxyAgent':
        """
        Get an existing ProxyAgent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_by: The actor who created the proxy agent.
        :param pulumi.Input[str] display_name: Proxy agent name.
        :param pulumi.Input[str] group_region: Data processing location. This is where Fivetran will operate and run computation on data.
        :param pulumi.Input[str] proxy_server_uri: The proxy server URI.
        :param pulumi.Input[str] registred_at: The timestamp of the time the proxy agent was created in your account.
        :param pulumi.Input[str] salt: The salt.
        :param pulumi.Input[str] token: The auth token.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProxyAgentState.__new__(_ProxyAgentState)

        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["group_region"] = group_region
        __props__.__dict__["proxy_server_uri"] = proxy_server_uri
        __props__.__dict__["registred_at"] = registred_at
        __props__.__dict__["salt"] = salt
        __props__.__dict__["token"] = token
        return ProxyAgent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        The actor who created the proxy agent.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Proxy agent name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="groupRegion")
    def group_region(self) -> pulumi.Output[str]:
        """
        Data processing location. This is where Fivetran will operate and run computation on data.
        """
        return pulumi.get(self, "group_region")

    @property
    @pulumi.getter(name="proxyServerUri")
    def proxy_server_uri(self) -> pulumi.Output[str]:
        """
        The proxy server URI.
        """
        return pulumi.get(self, "proxy_server_uri")

    @property
    @pulumi.getter(name="registredAt")
    def registred_at(self) -> pulumi.Output[str]:
        """
        The timestamp of the time the proxy agent was created in your account.
        """
        return pulumi.get(self, "registred_at")

    @property
    @pulumi.getter
    def salt(self) -> pulumi.Output[str]:
        """
        The salt.
        """
        return pulumi.get(self, "salt")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        The auth token.
        """
        return pulumi.get(self, "token")
