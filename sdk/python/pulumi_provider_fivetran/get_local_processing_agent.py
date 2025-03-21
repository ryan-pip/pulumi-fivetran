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

__all__ = [
    'GetLocalProcessingAgentResult',
    'AwaitableGetLocalProcessingAgentResult',
    'get_local_processing_agent',
    'get_local_processing_agent_output',
]

@pulumi.output_type
class GetLocalProcessingAgentResult:
    """
    A collection of values returned by getLocalProcessingAgent.
    """
    def __init__(__self__, display_name=None, group_id=None, id=None, registered_at=None, usages=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if group_id and not isinstance(group_id, str):
            raise TypeError("Expected argument 'group_id' to be a str")
        pulumi.set(__self__, "group_id", group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if registered_at and not isinstance(registered_at, str):
            raise TypeError("Expected argument 'registered_at' to be a str")
        pulumi.set(__self__, "registered_at", registered_at)
        if usages and not isinstance(usages, list):
            raise TypeError("Expected argument 'usages' to be a list")
        pulumi.set(__self__, "usages", usages)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The unique name for the local processing agent.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> str:
        """
        The unique identifier for the Group within the Fivetran system.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique identifier for the local processing agent within your account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="registeredAt")
    def registered_at(self) -> str:
        """
        The timestamp of the time the local processing agent was created in your account.
        """
        return pulumi.get(self, "registered_at")

    @property
    @pulumi.getter
    def usages(self) -> Sequence['outputs.GetLocalProcessingAgentUsageResult']:
        return pulumi.get(self, "usages")


class AwaitableGetLocalProcessingAgentResult(GetLocalProcessingAgentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalProcessingAgentResult(
            display_name=self.display_name,
            group_id=self.group_id,
            id=self.id,
            registered_at=self.registered_at,
            usages=self.usages)


def get_local_processing_agent(id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalProcessingAgentResult:
    """
    NOTE: In connection with the general availability of the hybrid deployment functionality and in order to synchronize internal terminology, we have deprecate this data source.

    This data source returns a local processing agent object.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_fivetran as fivetran

    local_processing_agent = fivetran.get_local_processing_agent(id="local_processing_agent_id")
    ```


    :param str id: The unique identifier for the local processing agent within your account.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('fivetran:index/getLocalProcessingAgent:getLocalProcessingAgent', __args__, opts=opts, typ=GetLocalProcessingAgentResult).value

    return AwaitableGetLocalProcessingAgentResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        group_id=pulumi.get(__ret__, 'group_id'),
        id=pulumi.get(__ret__, 'id'),
        registered_at=pulumi.get(__ret__, 'registered_at'),
        usages=pulumi.get(__ret__, 'usages'))
def get_local_processing_agent_output(id: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetLocalProcessingAgentResult]:
    """
    NOTE: In connection with the general availability of the hybrid deployment functionality and in order to synchronize internal terminology, we have deprecate this data source.

    This data source returns a local processing agent object.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_fivetran as fivetran

    local_processing_agent = fivetran.get_local_processing_agent(id="local_processing_agent_id")
    ```


    :param str id: The unique identifier for the local processing agent within your account.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('fivetran:index/getLocalProcessingAgent:getLocalProcessingAgent', __args__, opts=opts, typ=GetLocalProcessingAgentResult)
    return __ret__.apply(lambda __response__: GetLocalProcessingAgentResult(
        display_name=pulumi.get(__response__, 'display_name'),
        group_id=pulumi.get(__response__, 'group_id'),
        id=pulumi.get(__response__, 'id'),
        registered_at=pulumi.get(__response__, 'registered_at'),
        usages=pulumi.get(__response__, 'usages')))
