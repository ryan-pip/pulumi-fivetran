// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fivetran

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/ryan-pip/pulumi-fivetran/sdk/go/fivetran/internal"
)

// This resource allows you to create, update, and delete user memberships in groups.
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
//			_, err := fivetran.NewGroupUsers(ctx, "groupUsers", &fivetran.GroupUsersArgs{
//				GroupId: pulumi.Any(fivetran_group.Group.Id),
//				Users: fivetran.GroupUsersUserArray{
//					&fivetran.GroupUsersUserArgs{
//						Email: pulumi.String("mail@example.com"),
//						Role:  pulumi.String("Destination Analyst"),
//					},
//					&fivetran.GroupUsersUserArgs{
//						Email: pulumi.String("another_mail@example.com"),
//						Role:  pulumi.String("Destination Analyst"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type GroupUsers struct {
	pulumi.CustomResourceState

	// The unique identifier for the Group within the Fivetran system.
	GroupId     pulumi.StringOutput       `pulumi:"groupId"`
	LastUpdated pulumi.StringOutput       `pulumi:"lastUpdated"`
	Users       GroupUsersUserArrayOutput `pulumi:"users"`
}

// NewGroupUsers registers a new resource with the given unique name, arguments, and options.
func NewGroupUsers(ctx *pulumi.Context,
	name string, args *GroupUsersArgs, opts ...pulumi.ResourceOption) (*GroupUsers, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.GroupId == nil {
		return nil, errors.New("invalid value for required argument 'GroupId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource GroupUsers
	err := ctx.RegisterResource("fivetran:index/groupUsers:GroupUsers", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGroupUsers gets an existing GroupUsers resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGroupUsers(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GroupUsersState, opts ...pulumi.ResourceOption) (*GroupUsers, error) {
	var resource GroupUsers
	err := ctx.ReadResource("fivetran:index/groupUsers:GroupUsers", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GroupUsers resources.
type groupUsersState struct {
	// The unique identifier for the Group within the Fivetran system.
	GroupId     *string          `pulumi:"groupId"`
	LastUpdated *string          `pulumi:"lastUpdated"`
	Users       []GroupUsersUser `pulumi:"users"`
}

type GroupUsersState struct {
	// The unique identifier for the Group within the Fivetran system.
	GroupId     pulumi.StringPtrInput
	LastUpdated pulumi.StringPtrInput
	Users       GroupUsersUserArrayInput
}

func (GroupUsersState) ElementType() reflect.Type {
	return reflect.TypeOf((*groupUsersState)(nil)).Elem()
}

type groupUsersArgs struct {
	// The unique identifier for the Group within the Fivetran system.
	GroupId string           `pulumi:"groupId"`
	Users   []GroupUsersUser `pulumi:"users"`
}

// The set of arguments for constructing a GroupUsers resource.
type GroupUsersArgs struct {
	// The unique identifier for the Group within the Fivetran system.
	GroupId pulumi.StringInput
	Users   GroupUsersUserArrayInput
}

func (GroupUsersArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*groupUsersArgs)(nil)).Elem()
}

type GroupUsersInput interface {
	pulumi.Input

	ToGroupUsersOutput() GroupUsersOutput
	ToGroupUsersOutputWithContext(ctx context.Context) GroupUsersOutput
}

func (*GroupUsers) ElementType() reflect.Type {
	return reflect.TypeOf((**GroupUsers)(nil)).Elem()
}

func (i *GroupUsers) ToGroupUsersOutput() GroupUsersOutput {
	return i.ToGroupUsersOutputWithContext(context.Background())
}

func (i *GroupUsers) ToGroupUsersOutputWithContext(ctx context.Context) GroupUsersOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupUsersOutput)
}

func (i *GroupUsers) ToOutput(ctx context.Context) pulumix.Output[*GroupUsers] {
	return pulumix.Output[*GroupUsers]{
		OutputState: i.ToGroupUsersOutputWithContext(ctx).OutputState,
	}
}

// GroupUsersArrayInput is an input type that accepts GroupUsersArray and GroupUsersArrayOutput values.
// You can construct a concrete instance of `GroupUsersArrayInput` via:
//
//	GroupUsersArray{ GroupUsersArgs{...} }
type GroupUsersArrayInput interface {
	pulumi.Input

	ToGroupUsersArrayOutput() GroupUsersArrayOutput
	ToGroupUsersArrayOutputWithContext(context.Context) GroupUsersArrayOutput
}

type GroupUsersArray []GroupUsersInput

func (GroupUsersArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GroupUsers)(nil)).Elem()
}

func (i GroupUsersArray) ToGroupUsersArrayOutput() GroupUsersArrayOutput {
	return i.ToGroupUsersArrayOutputWithContext(context.Background())
}

func (i GroupUsersArray) ToGroupUsersArrayOutputWithContext(ctx context.Context) GroupUsersArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupUsersArrayOutput)
}

func (i GroupUsersArray) ToOutput(ctx context.Context) pulumix.Output[[]*GroupUsers] {
	return pulumix.Output[[]*GroupUsers]{
		OutputState: i.ToGroupUsersArrayOutputWithContext(ctx).OutputState,
	}
}

// GroupUsersMapInput is an input type that accepts GroupUsersMap and GroupUsersMapOutput values.
// You can construct a concrete instance of `GroupUsersMapInput` via:
//
//	GroupUsersMap{ "key": GroupUsersArgs{...} }
type GroupUsersMapInput interface {
	pulumi.Input

	ToGroupUsersMapOutput() GroupUsersMapOutput
	ToGroupUsersMapOutputWithContext(context.Context) GroupUsersMapOutput
}

type GroupUsersMap map[string]GroupUsersInput

func (GroupUsersMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GroupUsers)(nil)).Elem()
}

func (i GroupUsersMap) ToGroupUsersMapOutput() GroupUsersMapOutput {
	return i.ToGroupUsersMapOutputWithContext(context.Background())
}

func (i GroupUsersMap) ToGroupUsersMapOutputWithContext(ctx context.Context) GroupUsersMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupUsersMapOutput)
}

func (i GroupUsersMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*GroupUsers] {
	return pulumix.Output[map[string]*GroupUsers]{
		OutputState: i.ToGroupUsersMapOutputWithContext(ctx).OutputState,
	}
}

type GroupUsersOutput struct{ *pulumi.OutputState }

func (GroupUsersOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GroupUsers)(nil)).Elem()
}

func (o GroupUsersOutput) ToGroupUsersOutput() GroupUsersOutput {
	return o
}

func (o GroupUsersOutput) ToGroupUsersOutputWithContext(ctx context.Context) GroupUsersOutput {
	return o
}

func (o GroupUsersOutput) ToOutput(ctx context.Context) pulumix.Output[*GroupUsers] {
	return pulumix.Output[*GroupUsers]{
		OutputState: o.OutputState,
	}
}

// The unique identifier for the Group within the Fivetran system.
func (o GroupUsersOutput) GroupId() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupUsers) pulumi.StringOutput { return v.GroupId }).(pulumi.StringOutput)
}

func (o GroupUsersOutput) LastUpdated() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupUsers) pulumi.StringOutput { return v.LastUpdated }).(pulumi.StringOutput)
}

func (o GroupUsersOutput) Users() GroupUsersUserArrayOutput {
	return o.ApplyT(func(v *GroupUsers) GroupUsersUserArrayOutput { return v.Users }).(GroupUsersUserArrayOutput)
}

type GroupUsersArrayOutput struct{ *pulumi.OutputState }

func (GroupUsersArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GroupUsers)(nil)).Elem()
}

func (o GroupUsersArrayOutput) ToGroupUsersArrayOutput() GroupUsersArrayOutput {
	return o
}

func (o GroupUsersArrayOutput) ToGroupUsersArrayOutputWithContext(ctx context.Context) GroupUsersArrayOutput {
	return o
}

func (o GroupUsersArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*GroupUsers] {
	return pulumix.Output[[]*GroupUsers]{
		OutputState: o.OutputState,
	}
}

func (o GroupUsersArrayOutput) Index(i pulumi.IntInput) GroupUsersOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *GroupUsers {
		return vs[0].([]*GroupUsers)[vs[1].(int)]
	}).(GroupUsersOutput)
}

type GroupUsersMapOutput struct{ *pulumi.OutputState }

func (GroupUsersMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GroupUsers)(nil)).Elem()
}

func (o GroupUsersMapOutput) ToGroupUsersMapOutput() GroupUsersMapOutput {
	return o
}

func (o GroupUsersMapOutput) ToGroupUsersMapOutputWithContext(ctx context.Context) GroupUsersMapOutput {
	return o
}

func (o GroupUsersMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*GroupUsers] {
	return pulumix.Output[map[string]*GroupUsers]{
		OutputState: o.OutputState,
	}
}

func (o GroupUsersMapOutput) MapIndex(k pulumi.StringInput) GroupUsersOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *GroupUsers {
		return vs[0].(map[string]*GroupUsers)[vs[1].(string)]
	}).(GroupUsersOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GroupUsersInput)(nil)).Elem(), &GroupUsers{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupUsersArrayInput)(nil)).Elem(), GroupUsersArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupUsersMapInput)(nil)).Elem(), GroupUsersMap{})
	pulumi.RegisterOutputType(GroupUsersOutput{})
	pulumi.RegisterOutputType(GroupUsersArrayOutput{})
	pulumi.RegisterOutputType(GroupUsersMapOutput{})
}