// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * This data source returns a webhook object.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fivetran from "@pulumi/fivetran";
 *
 * const webhook = fivetran.getWebhook({
 *     id: "webhook_id",
 * });
 * ```
 */
export function getWebhook(args: GetWebhookArgs, opts?: pulumi.InvokeOptions): Promise<GetWebhookResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("fivetran:index/getWebhook:getWebhook", {
        "id": args.id,
        "runTests": args.runTests,
    }, opts);
}

/**
 * A collection of arguments for invoking getWebhook.
 */
export interface GetWebhookArgs {
    /**
     * The webhook ID
     */
    id: string;
    /**
     * Specifies whether the setup tests should be run
     */
    runTests?: boolean;
}

/**
 * A collection of values returned by getWebhook.
 */
export interface GetWebhookResult {
    /**
     * Boolean, if set to true, webhooks are immediately sent in response to events
     */
    readonly active: boolean;
    /**
     * The webhook creation timestamp
     */
    readonly createdAt: string;
    /**
     * The ID of the user who created the webhook.
     */
    readonly createdBy: string;
    /**
     * The array of event types
     */
    readonly events: string[];
    /**
     * The group ID
     */
    readonly groupId: string;
    /**
     * The webhook ID
     */
    readonly id: string;
    /**
     * Specifies whether the setup tests should be run
     */
    readonly runTests?: boolean;
    /**
     * The secret string used for payload signing and masked in the response.
     */
    readonly secret: string;
    /**
     * The webhook type (group, account)
     */
    readonly type: string;
    /**
     * Your webhooks URL endpoint for your application
     */
    readonly url: string;
}
/**
 * This data source returns a webhook object.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fivetran from "@pulumi/fivetran";
 *
 * const webhook = fivetran.getWebhook({
 *     id: "webhook_id",
 * });
 * ```
 */
export function getWebhookOutput(args: GetWebhookOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetWebhookResult> {
    return pulumi.output(args).apply((a: any) => getWebhook(a, opts))
}

/**
 * A collection of arguments for invoking getWebhook.
 */
export interface GetWebhookOutputArgs {
    /**
     * The webhook ID
     */
    id: pulumi.Input<string>;
    /**
     * Specifies whether the setup tests should be run
     */
    runTests?: pulumi.Input<boolean>;
}