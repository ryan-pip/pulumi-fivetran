// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fivetran

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/ryan-pip/pulumi-fivetran/sdk/go/fivetran/internal"
)

// This data source returns a webhook object.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/ryan-pip/pulumi-fivetran/sdk/go/fivetran"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := fivetran.LookupWebhook(ctx, &fivetran.LookupWebhookArgs{
//				Id: "webhook_id",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupWebhook(ctx *pulumi.Context, args *LookupWebhookArgs, opts ...pulumi.InvokeOption) (*LookupWebhookResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupWebhookResult
	err := ctx.Invoke("fivetran:index/getWebhook:getWebhook", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getWebhook.
type LookupWebhookArgs struct {
	// The webhook ID
	Id string `pulumi:"id"`
	// Specifies whether the setup tests should be run
	RunTests *bool `pulumi:"runTests"`
}

// A collection of values returned by getWebhook.
type LookupWebhookResult struct {
	// Boolean, if set to true, webhooks are immediately sent in response to events
	Active bool `pulumi:"active"`
	// The webhook creation timestamp
	CreatedAt string `pulumi:"createdAt"`
	// The ID of the user who created the webhook.
	CreatedBy string `pulumi:"createdBy"`
	// The array of event types
	Events []string `pulumi:"events"`
	// The group ID
	GroupId string `pulumi:"groupId"`
	// The webhook ID
	Id string `pulumi:"id"`
	// Specifies whether the setup tests should be run
	RunTests *bool `pulumi:"runTests"`
	// The secret string used for payload signing and masked in the response.
	Secret string `pulumi:"secret"`
	// The webhook type (group, account)
	Type string `pulumi:"type"`
	// Your webhooks URL endpoint for your application
	Url string `pulumi:"url"`
}

func LookupWebhookOutput(ctx *pulumi.Context, args LookupWebhookOutputArgs, opts ...pulumi.InvokeOption) LookupWebhookResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupWebhookResult, error) {
			args := v.(LookupWebhookArgs)
			r, err := LookupWebhook(ctx, &args, opts...)
			var s LookupWebhookResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupWebhookResultOutput)
}

// A collection of arguments for invoking getWebhook.
type LookupWebhookOutputArgs struct {
	// The webhook ID
	Id pulumi.StringInput `pulumi:"id"`
	// Specifies whether the setup tests should be run
	RunTests pulumi.BoolPtrInput `pulumi:"runTests"`
}

func (LookupWebhookOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWebhookArgs)(nil)).Elem()
}

// A collection of values returned by getWebhook.
type LookupWebhookResultOutput struct{ *pulumi.OutputState }

func (LookupWebhookResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWebhookResult)(nil)).Elem()
}

func (o LookupWebhookResultOutput) ToLookupWebhookResultOutput() LookupWebhookResultOutput {
	return o
}

func (o LookupWebhookResultOutput) ToLookupWebhookResultOutputWithContext(ctx context.Context) LookupWebhookResultOutput {
	return o
}

func (o LookupWebhookResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupWebhookResult] {
	return pulumix.Output[LookupWebhookResult]{
		OutputState: o.OutputState,
	}
}

// Boolean, if set to true, webhooks are immediately sent in response to events
func (o LookupWebhookResultOutput) Active() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupWebhookResult) bool { return v.Active }).(pulumi.BoolOutput)
}

// The webhook creation timestamp
func (o LookupWebhookResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWebhookResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The ID of the user who created the webhook.
func (o LookupWebhookResultOutput) CreatedBy() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWebhookResult) string { return v.CreatedBy }).(pulumi.StringOutput)
}

// The array of event types
func (o LookupWebhookResultOutput) Events() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupWebhookResult) []string { return v.Events }).(pulumi.StringArrayOutput)
}

// The group ID
func (o LookupWebhookResultOutput) GroupId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWebhookResult) string { return v.GroupId }).(pulumi.StringOutput)
}

// The webhook ID
func (o LookupWebhookResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWebhookResult) string { return v.Id }).(pulumi.StringOutput)
}

// Specifies whether the setup tests should be run
func (o LookupWebhookResultOutput) RunTests() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupWebhookResult) *bool { return v.RunTests }).(pulumi.BoolPtrOutput)
}

// The secret string used for payload signing and masked in the response.
func (o LookupWebhookResultOutput) Secret() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWebhookResult) string { return v.Secret }).(pulumi.StringOutput)
}

// The webhook type (group, account)
func (o LookupWebhookResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWebhookResult) string { return v.Type }).(pulumi.StringOutput)
}

// Your webhooks URL endpoint for your application
func (o LookupWebhookResultOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v LookupWebhookResult) string { return v.Url }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupWebhookResultOutput{})
}