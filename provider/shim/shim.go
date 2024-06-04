package shim

import (
	p "github.com/fivetran/terraform-provider-fivetran/fivetran/framework"
	"github.com/hashicorp/terraform-plugin-framework/provider"
)

func NewProvider() provider.Provider {
	return p.FivetranProvider()
}
