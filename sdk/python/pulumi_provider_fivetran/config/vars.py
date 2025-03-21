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
from .. import _utilities

import types

__config__ = pulumi.Config('fivetran')


class _ExportableConfig(types.ModuleType):
    @property
    def api_key(self) -> Optional[str]:
        return __config__.get('apiKey') or _utilities.get_env('FIVETRAN_API_KEY')

    @property
    def api_secret(self) -> Optional[str]:
        return __config__.get('apiSecret') or _utilities.get_env('FIVETRAN_API_SECRET')

    @property
    def api_url(self) -> Optional[str]:
        return __config__.get('apiUrl')

