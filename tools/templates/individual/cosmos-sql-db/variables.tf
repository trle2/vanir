variable "resource_group_name" {
  description = "The resource group name for this cosmos db"
  type        = string
}

variable "cosmos_account_name" {
  description = "CosmosDB account name"
  type        = string
}

variable "cosmos_db_offer_type" {
  type    = string
  default = "Standard"
}

variable "cosmos_consistency_level" {
  description = "consistency level of cosmos db"
  type        = string
  default     = "Session"
}

variable "max_interval_in_seconds" {
  description = "max interval in seconds. Only used when consistency level is BoundedStaleness"
  type        = number
  default     = 5
}

variable "max_staleness_prefix" {
  description = "max staleness prefix. Only used when consistency level is BoundedStaleness"
  type        = number
  default     = 200
}