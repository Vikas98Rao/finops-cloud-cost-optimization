# Azure Policy - Mandatory Tag Enforcement
# Author: Vikas Rao | Senior DevOps Engineer

resource "azurerm_policy_definition" "require_tags" {
  name         = "require-mandatory-tags"
  policy_type  = "Custom"
  mode         = "All"
  display_name = "Require mandatory resource tags"
  description  = "Enforces mandatory tagging standard: Environment, Owner, CostCenter, Project, ManagedBy"

  metadata = jsonencode({
    version  = "1.0.0"
    category = "Tags"
  })

  policy_rule = jsonencode({
    if = {
      allOf = [
        { field = "type", notEquals = "Microsoft.Resources/subscriptions/resourceGroups" },
        {
          anyOf = [
            { field = "tags['Environment']", exists = "false" },
            { field = "tags['Owner']",       exists = "false" },
            { field = "tags['CostCenter']",  exists = "false" },
            { field = "tags['Project']",     exists = "false" }
          ]
        }
      ]
    }
    then = {
      effect = "Deny"
    }
  })
}

resource "azurerm_management_group_policy_assignment" "require_tags" {
  name                 = "require-mandatory-tags"
  policy_definition_id = azurerm_policy_definition.require_tags.id
  management_group_id  = var.management_group_id
  display_name         = "Require mandatory tags - FinOps governance"
  description          = "Deployed by Vikas Rao - FinOps cost governance"
  enforce              = true
}