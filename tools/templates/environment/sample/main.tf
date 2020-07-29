data "azurerm_resource_group" "global_rg" {
  name = var.resource_group_name
}

data "azurerm_subscription" "primary" {
}

data "azurerm_client_config" "current" {
}

resource "azurerm_cosmosdb_sql_database" "storage_service" {
  name                = var.cosmos_sql_db_name
  resource_group_name = data.azurerm_resource_group.global_rg.name
  account_name        = var.cosmos_account_name
}

resource "azurerm_search_service" "storage_service" {
  name                = format("%s%s", var.resource_name_prefix, "-search")
  resource_group_name = data.azurerm_resource_group.global_rg.name
  location            = data.azurerm_resource_group.global_rg.location
  sku                 = var.search_service_sku
}

resource "azurerm_storage_account" "storage_service" {
  name                     = var.storage_service_account_name
  resource_group_name      = data.azurerm_resource_group.global_rg.name
  location                 = data.azurerm_resource_group.global_rg.location
  account_kind             = var.storage_account_account_kind
  account_tier             = var.storage_account_tier
  account_replication_type = var.storage_account_replication_type
}

resource "azurerm_storage_table" "storage_service" {
  name                 = "StorageServiceLookup"
  storage_account_name = azurerm_storage_account.storage_service.name
}

resource "azurerm_role_assignment" "storage_service_blob_role" {
  scope                            = data.azurerm_resource_group.global_rg.id
  role_definition_name             = "Storage Blob Data Contributor"
  principal_id                     = var.service_principal_object_id
  skip_service_principal_aad_check = true
}