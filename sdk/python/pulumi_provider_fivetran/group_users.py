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

__all__ = ['GroupUsersArgs', 'GroupUsers']

@pulumi.input_type
class GroupUsersArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 users: Optional[pulumi.Input[Sequence[pulumi.Input['GroupUsersUserArgs']]]] = None):
        """
        The set of arguments for constructing a GroupUsers resource.
        :param pulumi.Input[str] group_id: The unique identifier for the Group within the Fivetran system.
        """
        pulumi.set(__self__, "group_id", group_id)
        if users is not None:
            pulumi.set(__self__, "users", users)

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
    @pulumi.getter
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GroupUsersUserArgs']]]]:
        return pulumi.get(self, "users")

    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GroupUsersUserArgs']]]]):
        pulumi.set(self, "users", value)


@pulumi.input_type
class _GroupUsersState:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input['GroupUsersUserArgs']]]] = None):
        """
        Input properties used for looking up and filtering GroupUsers resources.
        :param pulumi.Input[str] group_id: The unique identifier for the Group within the Fivetran system.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if last_updated is not None:
            pulumi.set(__self__, "last_updated", last_updated)
        if users is not None:
            pulumi.set(__self__, "users", users)

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
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "last_updated")

    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated", value)

    @property
    @pulumi.getter
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GroupUsersUserArgs']]]]:
        return pulumi.get(self, "users")

    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GroupUsersUserArgs']]]]):
        pulumi.set(self, "users", value)


class GroupUsers(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[Union['GroupUsersUserArgs', 'GroupUsersUserArgsDict']]]]] = None,
                 __props__=None):
        """
        This resource allows you to create, update, and delete user memberships in groups.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_provider_fivetran as fivetran

        group_users = fivetran.GroupUsers("groupUsers",
            group_id=fivetran_group["group"]["id"],
            users=[
                {
                    "email": "mail@example.com",
                    "role": "Destination Analyst",
                },
                {
                    "email": "another_mail@example.com",
                    "role": "Destination Analyst",
                },
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The unique identifier for the Group within the Fivetran system.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupUsersArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to create, update, and delete user memberships in groups.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_provider_fivetran as fivetran

        group_users = fivetran.GroupUsers("groupUsers",
            group_id=fivetran_group["group"]["id"],
            users=[
                {
                    "email": "mail@example.com",
                    "role": "Destination Analyst",
                },
                {
                    "email": "another_mail@example.com",
                    "role": "Destination Analyst",
                },
            ])
        ```

        :param str resource_name: The name of the resource.
        :param GroupUsersArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupUsersArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[Union['GroupUsersUserArgs', 'GroupUsersUserArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupUsersArgs.__new__(GroupUsersArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["users"] = users
            __props__.__dict__["last_updated"] = None
        super(GroupUsers, __self__).__init__(
            'fivetran:index/groupUsers:GroupUsers',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            last_updated: Optional[pulumi.Input[str]] = None,
            users: Optional[pulumi.Input[Sequence[pulumi.Input[Union['GroupUsersUserArgs', 'GroupUsersUserArgsDict']]]]] = None) -> 'GroupUsers':
        """
        Get an existing GroupUsers resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The unique identifier for the Group within the Fivetran system.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupUsersState.__new__(_GroupUsersState)

        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["last_updated"] = last_updated
        __props__.__dict__["users"] = users
        return GroupUsers(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The unique identifier for the Group within the Fivetran system.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_updated")

    @property
    @pulumi.getter
    def users(self) -> pulumi.Output[Optional[Sequence['outputs.GroupUsersUser']]]:
        return pulumi.get(self, "users")

