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

// ## Import
//
// ### How to authorize connector
type Connector struct {
	pulumi.CustomResourceState

	Auth   ConnectorAuthPtrOutput `pulumi:"auth"`
	Config ConnectorConfigOutput  `pulumi:"config"`
	// The unique identifier of the user who has created the connector in your account
	ConnectedBy pulumi.StringOutput `pulumi:"connectedBy"`
	// The timestamp of the time the connector was created in your account
	CreatedAt         pulumi.StringOutput              `pulumi:"createdAt"`
	DestinationSchema ConnectorDestinationSchemaOutput `pulumi:"destinationSchema"`
	// The unique identifier for the Group (Destination) within the Fivetran system.
	GroupId     pulumi.StringOutput `pulumi:"groupId"`
	LastUpdated pulumi.StringOutput `pulumi:"lastUpdated"`
	// The name used both as the connector's name within the Fivetran system and as the source schema's name within your
	// destination.
	Name pulumi.StringOutput `pulumi:"name"`
	// Specifies whether the setup tests should be run automatically. The default value is TRUE.
	RunSetupTests pulumi.StringPtrOutput `pulumi:"runSetupTests"`
	// The connector type name within the Fivetran system.
	Service pulumi.StringOutput `pulumi:"service"`
	// Specifies whether we should trust the certificate automatically. The default value is FALSE. If a certificate is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// certificate](https://fivetran.com/docs/rest-api/certificates#approveadestinationcertificate).
	TrustCertificates pulumi.StringPtrOutput `pulumi:"trustCertificates"`
	// Specifies whether we should trust the SSH fingerprint automatically. The default value is FALSE. If a fingerprint is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// fingerprint](https://fivetran.com/docs/rest-api/certificates#approveadestinationfingerprint).
	TrustFingerprints pulumi.StringPtrOutput `pulumi:"trustFingerprints"`
}

// NewConnector registers a new resource with the given unique name, arguments, and options.
func NewConnector(ctx *pulumi.Context,
	name string, args *ConnectorArgs, opts ...pulumi.ResourceOption) (*Connector, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DestinationSchema == nil {
		return nil, errors.New("invalid value for required argument 'DestinationSchema'")
	}
	if args.GroupId == nil {
		return nil, errors.New("invalid value for required argument 'GroupId'")
	}
	if args.Service == nil {
		return nil, errors.New("invalid value for required argument 'Service'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Connector
	err := ctx.RegisterResource("fivetran:index/connector:Connector", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConnector gets an existing Connector resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConnector(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConnectorState, opts ...pulumi.ResourceOption) (*Connector, error) {
	var resource Connector
	err := ctx.ReadResource("fivetran:index/connector:Connector", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Connector resources.
type connectorState struct {
	Auth   *ConnectorAuth   `pulumi:"auth"`
	Config *ConnectorConfig `pulumi:"config"`
	// The unique identifier of the user who has created the connector in your account
	ConnectedBy *string `pulumi:"connectedBy"`
	// The timestamp of the time the connector was created in your account
	CreatedAt         *string                     `pulumi:"createdAt"`
	DestinationSchema *ConnectorDestinationSchema `pulumi:"destinationSchema"`
	// The unique identifier for the Group (Destination) within the Fivetran system.
	GroupId     *string `pulumi:"groupId"`
	LastUpdated *string `pulumi:"lastUpdated"`
	// The name used both as the connector's name within the Fivetran system and as the source schema's name within your
	// destination.
	Name *string `pulumi:"name"`
	// Specifies whether the setup tests should be run automatically. The default value is TRUE.
	RunSetupTests *string `pulumi:"runSetupTests"`
	// The connector type name within the Fivetran system.
	Service *string `pulumi:"service"`
	// Specifies whether we should trust the certificate automatically. The default value is FALSE. If a certificate is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// certificate](https://fivetran.com/docs/rest-api/certificates#approveadestinationcertificate).
	TrustCertificates *string `pulumi:"trustCertificates"`
	// Specifies whether we should trust the SSH fingerprint automatically. The default value is FALSE. If a fingerprint is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// fingerprint](https://fivetran.com/docs/rest-api/certificates#approveadestinationfingerprint).
	TrustFingerprints *string `pulumi:"trustFingerprints"`
}

type ConnectorState struct {
	Auth   ConnectorAuthPtrInput
	Config ConnectorConfigPtrInput
	// The unique identifier of the user who has created the connector in your account
	ConnectedBy pulumi.StringPtrInput
	// The timestamp of the time the connector was created in your account
	CreatedAt         pulumi.StringPtrInput
	DestinationSchema ConnectorDestinationSchemaPtrInput
	// The unique identifier for the Group (Destination) within the Fivetran system.
	GroupId     pulumi.StringPtrInput
	LastUpdated pulumi.StringPtrInput
	// The name used both as the connector's name within the Fivetran system and as the source schema's name within your
	// destination.
	Name pulumi.StringPtrInput
	// Specifies whether the setup tests should be run automatically. The default value is TRUE.
	RunSetupTests pulumi.StringPtrInput
	// The connector type name within the Fivetran system.
	Service pulumi.StringPtrInput
	// Specifies whether we should trust the certificate automatically. The default value is FALSE. If a certificate is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// certificate](https://fivetran.com/docs/rest-api/certificates#approveadestinationcertificate).
	TrustCertificates pulumi.StringPtrInput
	// Specifies whether we should trust the SSH fingerprint automatically. The default value is FALSE. If a fingerprint is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// fingerprint](https://fivetran.com/docs/rest-api/certificates#approveadestinationfingerprint).
	TrustFingerprints pulumi.StringPtrInput
}

func (ConnectorState) ElementType() reflect.Type {
	return reflect.TypeOf((*connectorState)(nil)).Elem()
}

type connectorArgs struct {
	Auth              *ConnectorAuth             `pulumi:"auth"`
	Config            *ConnectorConfig           `pulumi:"config"`
	DestinationSchema ConnectorDestinationSchema `pulumi:"destinationSchema"`
	// The unique identifier for the Group (Destination) within the Fivetran system.
	GroupId string `pulumi:"groupId"`
	// Specifies whether the setup tests should be run automatically. The default value is TRUE.
	RunSetupTests *string `pulumi:"runSetupTests"`
	// The connector type name within the Fivetran system.
	Service string `pulumi:"service"`
	// Specifies whether we should trust the certificate automatically. The default value is FALSE. If a certificate is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// certificate](https://fivetran.com/docs/rest-api/certificates#approveadestinationcertificate).
	TrustCertificates *string `pulumi:"trustCertificates"`
	// Specifies whether we should trust the SSH fingerprint automatically. The default value is FALSE. If a fingerprint is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// fingerprint](https://fivetran.com/docs/rest-api/certificates#approveadestinationfingerprint).
	TrustFingerprints *string `pulumi:"trustFingerprints"`
}

// The set of arguments for constructing a Connector resource.
type ConnectorArgs struct {
	Auth              ConnectorAuthPtrInput
	Config            ConnectorConfigPtrInput
	DestinationSchema ConnectorDestinationSchemaInput
	// The unique identifier for the Group (Destination) within the Fivetran system.
	GroupId pulumi.StringInput
	// Specifies whether the setup tests should be run automatically. The default value is TRUE.
	RunSetupTests pulumi.StringPtrInput
	// The connector type name within the Fivetran system.
	Service pulumi.StringInput
	// Specifies whether we should trust the certificate automatically. The default value is FALSE. If a certificate is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// certificate](https://fivetran.com/docs/rest-api/certificates#approveadestinationcertificate).
	TrustCertificates pulumi.StringPtrInput
	// Specifies whether we should trust the SSH fingerprint automatically. The default value is FALSE. If a fingerprint is not
	// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
	// fingerprint](https://fivetran.com/docs/rest-api/certificates#approveadestinationfingerprint).
	TrustFingerprints pulumi.StringPtrInput
}

func (ConnectorArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*connectorArgs)(nil)).Elem()
}

type ConnectorInput interface {
	pulumi.Input

	ToConnectorOutput() ConnectorOutput
	ToConnectorOutputWithContext(ctx context.Context) ConnectorOutput
}

func (*Connector) ElementType() reflect.Type {
	return reflect.TypeOf((**Connector)(nil)).Elem()
}

func (i *Connector) ToConnectorOutput() ConnectorOutput {
	return i.ToConnectorOutputWithContext(context.Background())
}

func (i *Connector) ToConnectorOutputWithContext(ctx context.Context) ConnectorOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorOutput)
}

func (i *Connector) ToOutput(ctx context.Context) pulumix.Output[*Connector] {
	return pulumix.Output[*Connector]{
		OutputState: i.ToConnectorOutputWithContext(ctx).OutputState,
	}
}

// ConnectorArrayInput is an input type that accepts ConnectorArray and ConnectorArrayOutput values.
// You can construct a concrete instance of `ConnectorArrayInput` via:
//
//	ConnectorArray{ ConnectorArgs{...} }
type ConnectorArrayInput interface {
	pulumi.Input

	ToConnectorArrayOutput() ConnectorArrayOutput
	ToConnectorArrayOutputWithContext(context.Context) ConnectorArrayOutput
}

type ConnectorArray []ConnectorInput

func (ConnectorArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Connector)(nil)).Elem()
}

func (i ConnectorArray) ToConnectorArrayOutput() ConnectorArrayOutput {
	return i.ToConnectorArrayOutputWithContext(context.Background())
}

func (i ConnectorArray) ToConnectorArrayOutputWithContext(ctx context.Context) ConnectorArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorArrayOutput)
}

func (i ConnectorArray) ToOutput(ctx context.Context) pulumix.Output[[]*Connector] {
	return pulumix.Output[[]*Connector]{
		OutputState: i.ToConnectorArrayOutputWithContext(ctx).OutputState,
	}
}

// ConnectorMapInput is an input type that accepts ConnectorMap and ConnectorMapOutput values.
// You can construct a concrete instance of `ConnectorMapInput` via:
//
//	ConnectorMap{ "key": ConnectorArgs{...} }
type ConnectorMapInput interface {
	pulumi.Input

	ToConnectorMapOutput() ConnectorMapOutput
	ToConnectorMapOutputWithContext(context.Context) ConnectorMapOutput
}

type ConnectorMap map[string]ConnectorInput

func (ConnectorMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Connector)(nil)).Elem()
}

func (i ConnectorMap) ToConnectorMapOutput() ConnectorMapOutput {
	return i.ToConnectorMapOutputWithContext(context.Background())
}

func (i ConnectorMap) ToConnectorMapOutputWithContext(ctx context.Context) ConnectorMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorMapOutput)
}

func (i ConnectorMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*Connector] {
	return pulumix.Output[map[string]*Connector]{
		OutputState: i.ToConnectorMapOutputWithContext(ctx).OutputState,
	}
}

type ConnectorOutput struct{ *pulumi.OutputState }

func (ConnectorOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Connector)(nil)).Elem()
}

func (o ConnectorOutput) ToConnectorOutput() ConnectorOutput {
	return o
}

func (o ConnectorOutput) ToConnectorOutputWithContext(ctx context.Context) ConnectorOutput {
	return o
}

func (o ConnectorOutput) ToOutput(ctx context.Context) pulumix.Output[*Connector] {
	return pulumix.Output[*Connector]{
		OutputState: o.OutputState,
	}
}

func (o ConnectorOutput) Auth() ConnectorAuthPtrOutput {
	return o.ApplyT(func(v *Connector) ConnectorAuthPtrOutput { return v.Auth }).(ConnectorAuthPtrOutput)
}

func (o ConnectorOutput) Config() ConnectorConfigOutput {
	return o.ApplyT(func(v *Connector) ConnectorConfigOutput { return v.Config }).(ConnectorConfigOutput)
}

// The unique identifier of the user who has created the connector in your account
func (o ConnectorOutput) ConnectedBy() pulumi.StringOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringOutput { return v.ConnectedBy }).(pulumi.StringOutput)
}

// The timestamp of the time the connector was created in your account
func (o ConnectorOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

func (o ConnectorOutput) DestinationSchema() ConnectorDestinationSchemaOutput {
	return o.ApplyT(func(v *Connector) ConnectorDestinationSchemaOutput { return v.DestinationSchema }).(ConnectorDestinationSchemaOutput)
}

// The unique identifier for the Group (Destination) within the Fivetran system.
func (o ConnectorOutput) GroupId() pulumi.StringOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringOutput { return v.GroupId }).(pulumi.StringOutput)
}

func (o ConnectorOutput) LastUpdated() pulumi.StringOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringOutput { return v.LastUpdated }).(pulumi.StringOutput)
}

// The name used both as the connector's name within the Fivetran system and as the source schema's name within your
// destination.
func (o ConnectorOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Specifies whether the setup tests should be run automatically. The default value is TRUE.
func (o ConnectorOutput) RunSetupTests() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringPtrOutput { return v.RunSetupTests }).(pulumi.StringPtrOutput)
}

// The connector type name within the Fivetran system.
func (o ConnectorOutput) Service() pulumi.StringOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringOutput { return v.Service }).(pulumi.StringOutput)
}

// Specifies whether we should trust the certificate automatically. The default value is FALSE. If a certificate is not
// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
// certificate](https://fivetran.com/docs/rest-api/certificates#approveadestinationcertificate).
func (o ConnectorOutput) TrustCertificates() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringPtrOutput { return v.TrustCertificates }).(pulumi.StringPtrOutput)
}

// Specifies whether we should trust the SSH fingerprint automatically. The default value is FALSE. If a fingerprint is not
// trusted automatically, it has to be approved with [Certificates Management API Approve a destination
// fingerprint](https://fivetran.com/docs/rest-api/certificates#approveadestinationfingerprint).
func (o ConnectorOutput) TrustFingerprints() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Connector) pulumi.StringPtrOutput { return v.TrustFingerprints }).(pulumi.StringPtrOutput)
}

type ConnectorArrayOutput struct{ *pulumi.OutputState }

func (ConnectorArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Connector)(nil)).Elem()
}

func (o ConnectorArrayOutput) ToConnectorArrayOutput() ConnectorArrayOutput {
	return o
}

func (o ConnectorArrayOutput) ToConnectorArrayOutputWithContext(ctx context.Context) ConnectorArrayOutput {
	return o
}

func (o ConnectorArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*Connector] {
	return pulumix.Output[[]*Connector]{
		OutputState: o.OutputState,
	}
}

func (o ConnectorArrayOutput) Index(i pulumi.IntInput) ConnectorOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Connector {
		return vs[0].([]*Connector)[vs[1].(int)]
	}).(ConnectorOutput)
}

type ConnectorMapOutput struct{ *pulumi.OutputState }

func (ConnectorMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Connector)(nil)).Elem()
}

func (o ConnectorMapOutput) ToConnectorMapOutput() ConnectorMapOutput {
	return o
}

func (o ConnectorMapOutput) ToConnectorMapOutputWithContext(ctx context.Context) ConnectorMapOutput {
	return o
}

func (o ConnectorMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*Connector] {
	return pulumix.Output[map[string]*Connector]{
		OutputState: o.OutputState,
	}
}

func (o ConnectorMapOutput) MapIndex(k pulumi.StringInput) ConnectorOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Connector {
		return vs[0].(map[string]*Connector)[vs[1].(string)]
	}).(ConnectorOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorInput)(nil)).Elem(), &Connector{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorArrayInput)(nil)).Elem(), ConnectorArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectorMapInput)(nil)).Elem(), ConnectorMap{})
	pulumi.RegisterOutputType(ConnectorOutput{})
	pulumi.RegisterOutputType(ConnectorArrayOutput{})
	pulumi.RegisterOutputType(ConnectorMapOutput{})
}