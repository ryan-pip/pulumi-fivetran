# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['UserGroupMembershipArgs', 'UserGroupMembership']

@pulumi.input_type
class UserGroupMembershipArgs:
    def __init__(__self__, *,
                 user_id: pulumi.Input[str],
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input['UserGroupMembershipGroupArgs']]]] = None):
        """
        The set of arguments for constructing a UserGroupMembership resource.
        :param pulumi.Input[str] user_id: The unique identifier for the user within your account.
        """
        pulumi.set(__self__, "user_id", user_id)
        if groups is not None:
            pulumi.set(__self__, "groups", groups)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        The unique identifier for the user within your account.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserGroupMembershipGroupArgs']]]]:
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserGroupMembershipGroupArgs']]]]):
        pulumi.set(self, "groups", value)


@pulumi.input_type
class _UserGroupMembershipState:
    def __init__(__self__, *,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input['UserGroupMembershipGroupArgs']]]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserGroupMembership resources.
        :param pulumi.Input[str] user_id: The unique identifier for the user within your account.
        """
        if groups is not None:
            pulumi.set(__self__, "groups", groups)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserGroupMembershipGroupArgs']]]]:
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserGroupMembershipGroupArgs']]]]):
        pulumi.set(self, "groups", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier for the user within your account.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class UserGroupMembership(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union['UserGroupMembershipGroupArgs', 'UserGroupMembershipGroupArgsDict']]]]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to create, update, and delete group membership for user

        ## Import

        1. To import an existing `fivetran_user_group_membership` resource into your Terraform state, you need to get `user_id` and `group_id`

        You can retrieve all users using the [fivetran_users data source](/docs/data-sources/users).

        2. Define an empty resource in your `.tf` configuration:

        hcl

        resource "fivetran_user_group_membership" "my_imported_fivetran_user_group_membership" {

        }

        3. Run the `pulumi import` command:

        ```sh
        $ pulumi import fivetran:index/userGroupMembership:UserGroupMembership my_imported_fivetran_user_group_membership {user_id}
        ```

        4. Use the `terraform state show` command to get the values from the state:

        terraform state show 'fivetran_user_group_membership.my_imported_fivetran_user_group_membership'

        5. Copy the values and paste them to your `.tf` configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] user_id: The unique identifier for the user within your account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserGroupMembershipArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to create, update, and delete group membership for user

        ## Import

        1. To import an existing `fivetran_user_group_membership` resource into your Terraform state, you need to get `user_id` and `group_id`

        You can retrieve all users using the [fivetran_users data source](/docs/data-sources/users).

        2. Define an empty resource in your `.tf` configuration:

        hcl

        resource "fivetran_user_group_membership" "my_imported_fivetran_user_group_membership" {

        }

        3. Run the `pulumi import` command:

        ```sh
        $ pulumi import fivetran:index/userGroupMembership:UserGroupMembership my_imported_fivetran_user_group_membership {user_id}
        ```

        4. Use the `terraform state show` command to get the values from the state:

        terraform state show 'fivetran_user_group_membership.my_imported_fivetran_user_group_membership'

        5. Copy the values and paste them to your `.tf` configuration.

        :param str resource_name: The name of the resource.
        :param UserGroupMembershipArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserGroupMembershipArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union['UserGroupMembershipGroupArgs', 'UserGroupMembershipGroupArgsDict']]]]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserGroupMembershipArgs.__new__(UserGroupMembershipArgs)

            __props__.__dict__["groups"] = groups
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
        super(UserGroupMembership, __self__).__init__(
            'fivetran:index/userGroupMembership:UserGroupMembership',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union['UserGroupMembershipGroupArgs', 'UserGroupMembershipGroupArgsDict']]]]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'UserGroupMembership':
        """
        Get an existing UserGroupMembership resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] user_id: The unique identifier for the user within your account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserGroupMembershipState.__new__(_UserGroupMembershipState)

        __props__.__dict__["groups"] = groups
        __props__.__dict__["user_id"] = user_id
        return UserGroupMembership(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Optional[Sequence['outputs.UserGroupMembershipGroup']]]:
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The unique identifier for the user within your account.
        """
        return pulumi.get(self, "user_id")
