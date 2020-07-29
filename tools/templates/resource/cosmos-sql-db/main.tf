#Simple CosmosDB/MongoDB deployment. No multiregion failover support.
provider "azurerm" {
  version = "~> 2.10"
	features {}
}

data "azurerm_resource_group" "default_rg" {
  name = var.resource_group_name
}

resource "azurerm_cosmosdb_account" "cosmosdb_account" {
  name                = var.cosmos_account_name
  location            = data.azurerm_resource_group.default_rg.location
  resource_group_name = data.azurerm_resource_group.default_rg.name
  offer_type          = var.cosmos_db_offer_type
  kind                = "GlobalDocumentDB"

  consistency_policy {
    consistency_level       = var.cosmos_consistency_level
    max_interval_in_seconds = var.cosmos_consistency_level == "BoundedStaleness" ? var.max_interval_in_seconds : 5
    max_staleness_prefix    = var.cosmos_consistency_level == "BoundedStaleness" ? var.max_staleness_prefix : 100
  }

  geo_location {
    location          = data.azurerm_resource_group.default_rg.location
    failover_priority = 0
  }
}