// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fivetran

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ryan-pip/pulumi-fivetran/sdk/go/fivetran/internal"
)

// This data source returns a hybrid deployment agent object.
func LookupHybridDeploymentAgent(ctx *pulumi.Context, args *LookupHybridDeploymentAgentArgs, opts ...pulumi.InvokeOption) (*LookupHybridDeploymentAgentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupHybridDeploymentAgentResult
	err := ctx.Invoke("fivetran:index/getHybridDeploymentAgent:getHybridDeploymentAgent", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getHybridDeploymentAgent.
type LookupHybridDeploymentAgentArgs struct {
	// The unique identifier for the hybrid deployment agent within your account.
	Id string `pulumi:"id"`
}

// A collection of values returned by getHybridDeploymentAgent.
type LookupHybridDeploymentAgentResult struct {
	// The unique name for the hybrid deployment agent.
	DisplayName string `pulumi:"displayName"`
	// The unique identifier for the Group within the Fivetran system.
	GroupId string `pulumi:"groupId"`
	// The unique identifier for the hybrid deployment agent within your account.
	Id string `pulumi:"id"`
	// The timestamp of the time the hybrid deployment agent was created in your account.
	RegisteredAt string `pulumi:"registeredAt"`
}

func LookupHybridDeploymentAgentOutput(ctx *pulumi.Context, args LookupHybridDeploymentAgentOutputArgs, opts ...pulumi.InvokeOption) LookupHybridDeploymentAgentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupHybridDeploymentAgentResultOutput, error) {
			args := v.(LookupHybridDeploymentAgentArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupHybridDeploymentAgentResult
			secret, err := ctx.InvokePackageRaw("fivetran:index/getHybridDeploymentAgent:getHybridDeploymentAgent", args, &rv, "", opts...)
			if err != nil {
				return LookupHybridDeploymentAgentResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupHybridDeploymentAgentResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupHybridDeploymentAgentResultOutput), nil
			}
			return output, nil
		}).(LookupHybridDeploymentAgentResultOutput)
}

// A collection of arguments for invoking getHybridDeploymentAgent.
type LookupHybridDeploymentAgentOutputArgs struct {
	// The unique identifier for the hybrid deployment agent within your account.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupHybridDeploymentAgentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupHybridDeploymentAgentArgs)(nil)).Elem()
}

// A collection of values returned by getHybridDeploymentAgent.
type LookupHybridDeploymentAgentResultOutput struct{ *pulumi.OutputState }

func (LookupHybridDeploymentAgentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupHybridDeploymentAgentResult)(nil)).Elem()
}

func (o LookupHybridDeploymentAgentResultOutput) ToLookupHybridDeploymentAgentResultOutput() LookupHybridDeploymentAgentResultOutput {
	return o
}

func (o LookupHybridDeploymentAgentResultOutput) ToLookupHybridDeploymentAgentResultOutputWithContext(ctx context.Context) LookupHybridDeploymentAgentResultOutput {
	return o
}

// The unique name for the hybrid deployment agent.
func (o LookupHybridDeploymentAgentResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHybridDeploymentAgentResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// The unique identifier for the Group within the Fivetran system.
func (o LookupHybridDeploymentAgentResultOutput) GroupId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHybridDeploymentAgentResult) string { return v.GroupId }).(pulumi.StringOutput)
}

// The unique identifier for the hybrid deployment agent within your account.
func (o LookupHybridDeploymentAgentResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHybridDeploymentAgentResult) string { return v.Id }).(pulumi.StringOutput)
}

// The timestamp of the time the hybrid deployment agent was created in your account.
func (o LookupHybridDeploymentAgentResultOutput) RegisteredAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHybridDeploymentAgentResult) string { return v.RegisteredAt }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupHybridDeploymentAgentResultOutput{})
}