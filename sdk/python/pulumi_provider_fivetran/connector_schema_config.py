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

__all__ = ['ConnectorSchemaConfigArgs', 'ConnectorSchemaConfig']

@pulumi.input_type
class ConnectorSchemaConfigArgs:
    def __init__(__self__, *,
                 connector_id: pulumi.Input[str],
                 schema_change_handling: pulumi.Input[str],
                 schema: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectorSchemaConfigSchemaArgs']]]] = None,
                 schemas: Optional[pulumi.Input[Mapping[str, pulumi.Input['ConnectorSchemaConfigSchemasArgs']]]] = None,
                 schemas_json: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['ConnectorSchemaConfigTimeoutsArgs']] = None,
                 validation_level: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConnectorSchemaConfig resource.
        :param pulumi.Input[str] connector_id: The unique identifier for the connector within the Fivetran system.
        :param pulumi.Input[str] schema_change_handling: The value specifying how new source data is handled.
        :param pulumi.Input[Mapping[str, pulumi.Input['ConnectorSchemaConfigSchemasArgs']]] schemas: Map of schema configurations.
        :param pulumi.Input[str] schemas_json: Schema settings in Json format, following Fivetran API endpoint contract for `schemas` field (a map of schemas).
        :param pulumi.Input[str] validation_level: The value defines validation method. - NONE: no validation, any configuration accepted. - TABLES: validate table names,
               fail on attempt to configure non-existing schemas/tables. - COLUMNS: validate the whole schema config including column
               names. The resource will try to fetch columns for every configured table and verify column names.
        """
        pulumi.set(__self__, "connector_id", connector_id)
        pulumi.set(__self__, "schema_change_handling", schema_change_handling)
        if schema is not None:
            warnings.warn("""Configure `schemas` instead. This attribute will be removed in the next major version of the provider.""", DeprecationWarning)
            pulumi.log.warn("""schema is deprecated: Configure `schemas` instead. This attribute will be removed in the next major version of the provider.""")
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if schemas is not None:
            pulumi.set(__self__, "schemas", schemas)
        if schemas_json is not None:
            pulumi.set(__self__, "schemas_json", schemas_json)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)
        if validation_level is not None:
            pulumi.set(__self__, "validation_level", validation_level)

    @property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Input[str]:
        """
        The unique identifier for the connector within the Fivetran system.
        """
        return pulumi.get(self, "connector_id")

    @connector_id.setter
    def connector_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "connector_id", value)

    @property
    @pulumi.getter(name="schemaChangeHandling")
    def schema_change_handling(self) -> pulumi.Input[str]:
        """
        The value specifying how new source data is handled.
        """
        return pulumi.get(self, "schema_change_handling")

    @schema_change_handling.setter
    def schema_change_handling(self, value: pulumi.Input[str]):
        pulumi.set(self, "schema_change_handling", value)

    @property
    @pulumi.getter
    @_utilities.deprecated("""Configure `schemas` instead. This attribute will be removed in the next major version of the provider.""")
    def schema(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectorSchemaConfigSchemaArgs']]]]:
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectorSchemaConfigSchemaArgs']]]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter
    def schemas(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ConnectorSchemaConfigSchemasArgs']]]]:
        """
        Map of schema configurations.
        """
        return pulumi.get(self, "schemas")

    @schemas.setter
    def schemas(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ConnectorSchemaConfigSchemasArgs']]]]):
        pulumi.set(self, "schemas", value)

    @property
    @pulumi.getter(name="schemasJson")
    def schemas_json(self) -> Optional[pulumi.Input[str]]:
        """
        Schema settings in Json format, following Fivetran API endpoint contract for `schemas` field (a map of schemas).
        """
        return pulumi.get(self, "schemas_json")

    @schemas_json.setter
    def schemas_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schemas_json", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['ConnectorSchemaConfigTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['ConnectorSchemaConfigTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)

    @property
    @pulumi.getter(name="validationLevel")
    def validation_level(self) -> Optional[pulumi.Input[str]]:
        """
        The value defines validation method. - NONE: no validation, any configuration accepted. - TABLES: validate table names,
        fail on attempt to configure non-existing schemas/tables. - COLUMNS: validate the whole schema config including column
        names. The resource will try to fetch columns for every configured table and verify column names.
        """
        return pulumi.get(self, "validation_level")

    @validation_level.setter
    def validation_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_level", value)


@pulumi.input_type
class _ConnectorSchemaConfigState:
    def __init__(__self__, *,
                 connector_id: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectorSchemaConfigSchemaArgs']]]] = None,
                 schema_change_handling: Optional[pulumi.Input[str]] = None,
                 schemas: Optional[pulumi.Input[Mapping[str, pulumi.Input['ConnectorSchemaConfigSchemasArgs']]]] = None,
                 schemas_json: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['ConnectorSchemaConfigTimeoutsArgs']] = None,
                 validation_level: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConnectorSchemaConfig resources.
        :param pulumi.Input[str] connector_id: The unique identifier for the connector within the Fivetran system.
        :param pulumi.Input[str] schema_change_handling: The value specifying how new source data is handled.
        :param pulumi.Input[Mapping[str, pulumi.Input['ConnectorSchemaConfigSchemasArgs']]] schemas: Map of schema configurations.
        :param pulumi.Input[str] schemas_json: Schema settings in Json format, following Fivetran API endpoint contract for `schemas` field (a map of schemas).
        :param pulumi.Input[str] validation_level: The value defines validation method. - NONE: no validation, any configuration accepted. - TABLES: validate table names,
               fail on attempt to configure non-existing schemas/tables. - COLUMNS: validate the whole schema config including column
               names. The resource will try to fetch columns for every configured table and verify column names.
        """
        if connector_id is not None:
            pulumi.set(__self__, "connector_id", connector_id)
        if schema is not None:
            warnings.warn("""Configure `schemas` instead. This attribute will be removed in the next major version of the provider.""", DeprecationWarning)
            pulumi.log.warn("""schema is deprecated: Configure `schemas` instead. This attribute will be removed in the next major version of the provider.""")
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if schema_change_handling is not None:
            pulumi.set(__self__, "schema_change_handling", schema_change_handling)
        if schemas is not None:
            pulumi.set(__self__, "schemas", schemas)
        if schemas_json is not None:
            pulumi.set(__self__, "schemas_json", schemas_json)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)
        if validation_level is not None:
            pulumi.set(__self__, "validation_level", validation_level)

    @property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier for the connector within the Fivetran system.
        """
        return pulumi.get(self, "connector_id")

    @connector_id.setter
    def connector_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_id", value)

    @property
    @pulumi.getter
    @_utilities.deprecated("""Configure `schemas` instead. This attribute will be removed in the next major version of the provider.""")
    def schema(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectorSchemaConfigSchemaArgs']]]]:
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectorSchemaConfigSchemaArgs']]]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="schemaChangeHandling")
    def schema_change_handling(self) -> Optional[pulumi.Input[str]]:
        """
        The value specifying how new source data is handled.
        """
        return pulumi.get(self, "schema_change_handling")

    @schema_change_handling.setter
    def schema_change_handling(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_change_handling", value)

    @property
    @pulumi.getter
    def schemas(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ConnectorSchemaConfigSchemasArgs']]]]:
        """
        Map of schema configurations.
        """
        return pulumi.get(self, "schemas")

    @schemas.setter
    def schemas(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ConnectorSchemaConfigSchemasArgs']]]]):
        pulumi.set(self, "schemas", value)

    @property
    @pulumi.getter(name="schemasJson")
    def schemas_json(self) -> Optional[pulumi.Input[str]]:
        """
        Schema settings in Json format, following Fivetran API endpoint contract for `schemas` field (a map of schemas).
        """
        return pulumi.get(self, "schemas_json")

    @schemas_json.setter
    def schemas_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schemas_json", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['ConnectorSchemaConfigTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['ConnectorSchemaConfigTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)

    @property
    @pulumi.getter(name="validationLevel")
    def validation_level(self) -> Optional[pulumi.Input[str]]:
        """
        The value defines validation method. - NONE: no validation, any configuration accepted. - TABLES: validate table names,
        fail on attempt to configure non-existing schemas/tables. - COLUMNS: validate the whole schema config including column
        names. The resource will try to fetch columns for every configured table and verify column names.
        """
        return pulumi.get(self, "validation_level")

    @validation_level.setter
    def validation_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_level", value)


class ConnectorSchemaConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_id: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ConnectorSchemaConfigSchemaArgs', 'ConnectorSchemaConfigSchemaArgsDict']]]]] = None,
                 schema_change_handling: Optional[pulumi.Input[str]] = None,
                 schemas: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ConnectorSchemaConfigSchemasArgs', 'ConnectorSchemaConfigSchemasArgsDict']]]]] = None,
                 schemas_json: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['ConnectorSchemaConfigTimeoutsArgs', 'ConnectorSchemaConfigTimeoutsArgsDict']]] = None,
                 validation_level: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        You don't need to import this resource as it is synthetic (doesn't create new instances in upstream).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connector_id: The unique identifier for the connector within the Fivetran system.
        :param pulumi.Input[str] schema_change_handling: The value specifying how new source data is handled.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['ConnectorSchemaConfigSchemasArgs', 'ConnectorSchemaConfigSchemasArgsDict']]]] schemas: Map of schema configurations.
        :param pulumi.Input[str] schemas_json: Schema settings in Json format, following Fivetran API endpoint contract for `schemas` field (a map of schemas).
        :param pulumi.Input[str] validation_level: The value defines validation method. - NONE: no validation, any configuration accepted. - TABLES: validate table names,
               fail on attempt to configure non-existing schemas/tables. - COLUMNS: validate the whole schema config including column
               names. The resource will try to fetch columns for every configured table and verify column names.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorSchemaConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        You don't need to import this resource as it is synthetic (doesn't create new instances in upstream).

        :param str resource_name: The name of the resource.
        :param ConnectorSchemaConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorSchemaConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_id: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ConnectorSchemaConfigSchemaArgs', 'ConnectorSchemaConfigSchemaArgsDict']]]]] = None,
                 schema_change_handling: Optional[pulumi.Input[str]] = None,
                 schemas: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ConnectorSchemaConfigSchemasArgs', 'ConnectorSchemaConfigSchemasArgsDict']]]]] = None,
                 schemas_json: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['ConnectorSchemaConfigTimeoutsArgs', 'ConnectorSchemaConfigTimeoutsArgsDict']]] = None,
                 validation_level: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorSchemaConfigArgs.__new__(ConnectorSchemaConfigArgs)

            if connector_id is None and not opts.urn:
                raise TypeError("Missing required property 'connector_id'")
            __props__.__dict__["connector_id"] = connector_id
            __props__.__dict__["schema"] = schema
            if schema_change_handling is None and not opts.urn:
                raise TypeError("Missing required property 'schema_change_handling'")
            __props__.__dict__["schema_change_handling"] = schema_change_handling
            __props__.__dict__["schemas"] = schemas
            __props__.__dict__["schemas_json"] = schemas_json
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["validation_level"] = validation_level
        super(ConnectorSchemaConfig, __self__).__init__(
            'fivetran:index/connectorSchemaConfig:ConnectorSchemaConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connector_id: Optional[pulumi.Input[str]] = None,
            schema: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ConnectorSchemaConfigSchemaArgs', 'ConnectorSchemaConfigSchemaArgsDict']]]]] = None,
            schema_change_handling: Optional[pulumi.Input[str]] = None,
            schemas: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['ConnectorSchemaConfigSchemasArgs', 'ConnectorSchemaConfigSchemasArgsDict']]]]] = None,
            schemas_json: Optional[pulumi.Input[str]] = None,
            timeouts: Optional[pulumi.Input[Union['ConnectorSchemaConfigTimeoutsArgs', 'ConnectorSchemaConfigTimeoutsArgsDict']]] = None,
            validation_level: Optional[pulumi.Input[str]] = None) -> 'ConnectorSchemaConfig':
        """
        Get an existing ConnectorSchemaConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connector_id: The unique identifier for the connector within the Fivetran system.
        :param pulumi.Input[str] schema_change_handling: The value specifying how new source data is handled.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['ConnectorSchemaConfigSchemasArgs', 'ConnectorSchemaConfigSchemasArgsDict']]]] schemas: Map of schema configurations.
        :param pulumi.Input[str] schemas_json: Schema settings in Json format, following Fivetran API endpoint contract for `schemas` field (a map of schemas).
        :param pulumi.Input[str] validation_level: The value defines validation method. - NONE: no validation, any configuration accepted. - TABLES: validate table names,
               fail on attempt to configure non-existing schemas/tables. - COLUMNS: validate the whole schema config including column
               names. The resource will try to fetch columns for every configured table and verify column names.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectorSchemaConfigState.__new__(_ConnectorSchemaConfigState)

        __props__.__dict__["connector_id"] = connector_id
        __props__.__dict__["schema"] = schema
        __props__.__dict__["schema_change_handling"] = schema_change_handling
        __props__.__dict__["schemas"] = schemas
        __props__.__dict__["schemas_json"] = schemas_json
        __props__.__dict__["timeouts"] = timeouts
        __props__.__dict__["validation_level"] = validation_level
        return ConnectorSchemaConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Output[str]:
        """
        The unique identifier for the connector within the Fivetran system.
        """
        return pulumi.get(self, "connector_id")

    @property
    @pulumi.getter
    @_utilities.deprecated("""Configure `schemas` instead. This attribute will be removed in the next major version of the provider.""")
    def schema(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectorSchemaConfigSchema']]]:
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="schemaChangeHandling")
    def schema_change_handling(self) -> pulumi.Output[str]:
        """
        The value specifying how new source data is handled.
        """
        return pulumi.get(self, "schema_change_handling")

    @property
    @pulumi.getter
    def schemas(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ConnectorSchemaConfigSchemas']]]:
        """
        Map of schema configurations.
        """
        return pulumi.get(self, "schemas")

    @property
    @pulumi.getter(name="schemasJson")
    def schemas_json(self) -> pulumi.Output[Optional[str]]:
        """
        Schema settings in Json format, following Fivetran API endpoint contract for `schemas` field (a map of schemas).
        """
        return pulumi.get(self, "schemas_json")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.ConnectorSchemaConfigTimeouts']]:
        return pulumi.get(self, "timeouts")

    @property
    @pulumi.getter(name="validationLevel")
    def validation_level(self) -> pulumi.Output[str]:
        """
        The value defines validation method. - NONE: no validation, any configuration accepted. - TABLES: validate table names,
        fail on attempt to configure non-existing schemas/tables. - COLUMNS: validate the whole schema config including column
        names. The resource will try to fetch columns for every configured table and verify column names.
        """
        return pulumi.get(self, "validation_level")
