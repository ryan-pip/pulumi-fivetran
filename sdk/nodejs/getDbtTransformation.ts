// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * This data source returns a dbt Transformation object.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fivetran from "@pulumi/fivetran";
 *
 * const transformation = fivetran.getDbtTransformation({
 *     id: "transformation_id",
 * });
 * ```
 */
export function getDbtTransformation(args: GetDbtTransformationArgs, opts?: pulumi.InvokeOptions): Promise<GetDbtTransformationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("fivetran:index/getDbtTransformation:getDbtTransformation", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getDbtTransformation.
 */
export interface GetDbtTransformationArgs {
    /**
     * The ID of this resource.
     */
    id: string;
}

/**
 * A collection of values returned by getDbtTransformation.
 */
export interface GetDbtTransformationResult {
    /**
     * Identifiers of related connectors.
     */
    readonly connectorIds: string[];
    /**
     * The timestamp of the dbt Transformation creation.
     */
    readonly createdAt: string;
    /**
     * The unique identifier for the dbt Model within the Fivetran system.
     */
    readonly dbtModelId: string;
    /**
     * Target dbt Model name.
     */
    readonly dbtModelName: string;
    /**
     * The unique identifier for the dbt Project within the Fivetran system.
     */
    readonly dbtProjectId: string;
    /**
     * The ID of this resource.
     */
    readonly id: string;
    /**
     * Identifiers of related models.
     */
    readonly modelIds: string[];
    /**
     * The dbt Model name.
     */
    readonly outputModelName: string;
    /**
     * The field indicating whether the transformation will be created in paused state. By default, the value is false.
     */
    readonly paused: boolean;
    /**
     * The field indicating whether the tests have been configured for dbt Transformation. By default, the value is false.
     */
    readonly runTests: boolean;
    /**
     * dbt Transformation schedule parameters.
     */
    readonly schedules: outputs.GetDbtTransformationSchedule[];
}
/**
 * This data source returns a dbt Transformation object.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fivetran from "@pulumi/fivetran";
 *
 * const transformation = fivetran.getDbtTransformation({
 *     id: "transformation_id",
 * });
 * ```
 */
export function getDbtTransformationOutput(args: GetDbtTransformationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDbtTransformationResult> {
    return pulumi.output(args).apply((a: any) => getDbtTransformation(a, opts))
}

/**
 * A collection of arguments for invoking getDbtTransformation.
 */
export interface GetDbtTransformationOutputArgs {
    /**
     * The ID of this resource.
     */
    id: pulumi.Input<string>;
}
