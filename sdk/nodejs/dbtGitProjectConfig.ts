// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Resource is in ALPHA state.
 *
 * This resource allows you to add and manage dbt Git Projects Configs.
 *
 * ## Import
 *
 * 1. To import an existing `fivetran_dbt_git_project_config` resource into your Terraform state, you need to get **Dbt Project ID** via API call `GET https://api.fivetran.com/v1/dbt/projects` to retrieve available projects.
 *
 * 2. Fetch project details for particular `project-id` using `GET https://api.fivetran.com/v1/dbt/projects/{project-id}` to ensure that this is the project you want to import.
 *
 * 3. Define an empty resource in your `.tf` configuration:
 *
 * hcl
 *
 * resource "fivetran_dbt_git_project_config" "my_imported_fivetran_dbt_git_project_config" {
 *
 * }
 *
 * 4. Run the `pulumi import` command:
 *
 * ```sh
 * $ pulumi import fivetran:index/dbtGitProjectConfig:DbtGitProjectConfig my_imported_fivetran_dbt_git_project_config {Dbt Project ID}
 * ```
 *
 * 4. Use the `terraform state show` command to get the values from the state:
 *
 * terraform state show 'fivetran_dbt_git_project_config.my_imported_fivetran_dbt_git_project_config'
 *
 * 5. Copy the values and paste them to your `.tf` configuration.
 */
export class DbtGitProjectConfig extends pulumi.CustomResource {
    /**
     * Get an existing DbtGitProjectConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DbtGitProjectConfigState, opts?: pulumi.CustomResourceOptions): DbtGitProjectConfig {
        return new DbtGitProjectConfig(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'fivetran:index/dbtGitProjectConfig:DbtGitProjectConfig';

    /**
     * Returns true if the given object is an instance of DbtGitProjectConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DbtGitProjectConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DbtGitProjectConfig.__pulumiType;
    }

    /**
     * Should resource wait for project to finish initialization. Default value: false.
     */
    public readonly ensureReadiness!: pulumi.Output<boolean>;
    /**
     * Folder in Git repo with your dbt project.
     */
    public readonly folderPath!: pulumi.Output<string | undefined>;
    /**
     * Git branch.
     */
    public readonly gitBranch!: pulumi.Output<string | undefined>;
    /**
     * Git remote URL with your dbt project.
     */
    public readonly gitRemoteUrl!: pulumi.Output<string | undefined>;
    /**
     * The unique identifier for the dbt Project within the Fivetran system.
     */
    public readonly projectId!: pulumi.Output<string>;

    /**
     * Create a DbtGitProjectConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DbtGitProjectConfigArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DbtGitProjectConfigArgs | DbtGitProjectConfigState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DbtGitProjectConfigState | undefined;
            resourceInputs["ensureReadiness"] = state ? state.ensureReadiness : undefined;
            resourceInputs["folderPath"] = state ? state.folderPath : undefined;
            resourceInputs["gitBranch"] = state ? state.gitBranch : undefined;
            resourceInputs["gitRemoteUrl"] = state ? state.gitRemoteUrl : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
        } else {
            const args = argsOrState as DbtGitProjectConfigArgs | undefined;
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            resourceInputs["ensureReadiness"] = args ? args.ensureReadiness : undefined;
            resourceInputs["folderPath"] = args ? args.folderPath : undefined;
            resourceInputs["gitBranch"] = args ? args.gitBranch : undefined;
            resourceInputs["gitRemoteUrl"] = args ? args.gitRemoteUrl : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DbtGitProjectConfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DbtGitProjectConfig resources.
 */
export interface DbtGitProjectConfigState {
    /**
     * Should resource wait for project to finish initialization. Default value: false.
     */
    ensureReadiness?: pulumi.Input<boolean>;
    /**
     * Folder in Git repo with your dbt project.
     */
    folderPath?: pulumi.Input<string>;
    /**
     * Git branch.
     */
    gitBranch?: pulumi.Input<string>;
    /**
     * Git remote URL with your dbt project.
     */
    gitRemoteUrl?: pulumi.Input<string>;
    /**
     * The unique identifier for the dbt Project within the Fivetran system.
     */
    projectId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DbtGitProjectConfig resource.
 */
export interface DbtGitProjectConfigArgs {
    /**
     * Should resource wait for project to finish initialization. Default value: false.
     */
    ensureReadiness?: pulumi.Input<boolean>;
    /**
     * Folder in Git repo with your dbt project.
     */
    folderPath?: pulumi.Input<string>;
    /**
     * Git branch.
     */
    gitBranch?: pulumi.Input<string>;
    /**
     * Git remote URL with your dbt project.
     */
    gitRemoteUrl?: pulumi.Input<string>;
    /**
     * The unique identifier for the dbt Project within the Fivetran system.
     */
    projectId: pulumi.Input<string>;
}