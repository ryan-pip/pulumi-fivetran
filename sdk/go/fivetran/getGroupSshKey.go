// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fivetran

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ryan-pip/pulumi-fivetran/sdk/go/fivetran/internal"
)

// This data source returns public key from SSH key pair associated with the group.
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
//			_, err := fivetran.GetGroupSshKey(ctx, &fivetran.GetGroupSshKeyArgs{
//				Id: "group_id",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetGroupSshKey(ctx *pulumi.Context, args *GetGroupSshKeyArgs, opts ...pulumi.InvokeOption) (*GetGroupSshKeyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetGroupSshKeyResult
	err := ctx.Invoke("fivetran:index/getGroupSshKey:getGroupSshKey", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGroupSshKey.
type GetGroupSshKeyArgs struct {
	// The unique identifier for the group within the Fivetran system.
	Id string `pulumi:"id"`
}

// A collection of values returned by getGroupSshKey.
type GetGroupSshKeyResult struct {
	// The unique identifier for the group within the Fivetran system.
	Id string `pulumi:"id"`
	// Public key from SSH key pair associated with the group.
	PublicKey string `pulumi:"publicKey"`
}

func GetGroupSshKeyOutput(ctx *pulumi.Context, args GetGroupSshKeyOutputArgs, opts ...pulumi.InvokeOption) GetGroupSshKeyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetGroupSshKeyResult, error) {
			args := v.(GetGroupSshKeyArgs)
			r, err := GetGroupSshKey(ctx, &args, opts...)
			var s GetGroupSshKeyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetGroupSshKeyResultOutput)
}

// A collection of arguments for invoking getGroupSshKey.
type GetGroupSshKeyOutputArgs struct {
	// The unique identifier for the group within the Fivetran system.
	Id pulumi.StringInput `pulumi:"id"`
}

func (GetGroupSshKeyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetGroupSshKeyArgs)(nil)).Elem()
}

// A collection of values returned by getGroupSshKey.
type GetGroupSshKeyResultOutput struct{ *pulumi.OutputState }

func (GetGroupSshKeyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetGroupSshKeyResult)(nil)).Elem()
}

func (o GetGroupSshKeyResultOutput) ToGetGroupSshKeyResultOutput() GetGroupSshKeyResultOutput {
	return o
}

func (o GetGroupSshKeyResultOutput) ToGetGroupSshKeyResultOutputWithContext(ctx context.Context) GetGroupSshKeyResultOutput {
	return o
}

// The unique identifier for the group within the Fivetran system.
func (o GetGroupSshKeyResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetGroupSshKeyResult) string { return v.Id }).(pulumi.StringOutput)
}

// Public key from SSH key pair associated with the group.
func (o GetGroupSshKeyResultOutput) PublicKey() pulumi.StringOutput {
	return o.ApplyT(func(v GetGroupSshKeyResult) string { return v.PublicKey }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetGroupSshKeyResultOutput{})
}