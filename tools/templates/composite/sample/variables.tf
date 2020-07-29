variable "resource_group_name" {
  description = "Default resource group name to use."
  type        = string
}

variable "resource_name_prefix" {
  description = "The prefix will be added to resource names."
  type        = string
}

variable "cosmos_account_name" {
  description = "CosmosDB account name"
  type        = string
}

variable "cosmos_sql_db_name" {
  description = "Sql database name"
  type        = string
}

variable "search_service_sku" {
  description = "The SKU which should be used for this Search Service. Possible values are basic, free, standard, standard2 and standard3."
  type        = string
  default     = "standard"
}

variable "storage_service_account_name" {
  description = "Specifies the name of the storage account. This must be unique across the entire Azure service, not just within the resource group."
  type        = string
}

variable "storage_account_account_kind" {
  description = "Defines the Kind of account. Valid options are BlobStorage, BlockBlobStorage, FileStorage, Storage and StorageV2."
  type        = string
  default     = "StorageV2"
}

variable "storage_account_tier" {
  description = "Defines the Tier to use for this storage account. Valid options are Standard and Premium."
  type        = string
  default     = "Standard"
}

variable "storage_account_replication_type" {
  description = "Defines the type of replication to use for this storage account. Valid options are LRS, GRS, RAGRS, ZRS, GZRS and RAGZRS."
  type        = string
  default     = "ZRS"
}

variable "service_principal_object_id" {
  description = "The service principal object id of EPMT Core Services."
  type = string
}