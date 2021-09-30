
data "azurerm_client_config" "current" {}


#Pytest Resource Group
resource "azurerm_resource_group" "pytest_rg" {
  name     = "pytest"
  location = "Canada Central"
}


#Pytest Keyvault
resource "azurerm_key_vault" "pytest_kv" {

  #Reequired
  name                       = "pytestKeyVault"
  location                   = azurerm_resource_group.pytest_rg.location
  resource_group_name        = azurerm_resource_group.pytest_rg.name
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "premium"
  soft_delete_retention_days = 7

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    key_permissions = [
      "create",
      "get",
    ]

    secret_permissions = [
      "set",
      "get",
      "delete",
      "purge",
      "recover"
    ]
  }
}


#storage12345_sa
resource "azurerm_storage_account" "storage12345_sa" {
  name                     = "storage12345storage12345"
  resource_group_name      = azurerm_resource_group.pytest_rg.name
  location                 = azurerm_resource_group.pytest_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "staging"
  }
}


resource "azurerm_storage_container" "storage1_container" {
  name                  = "file"
  storage_account_name  = azurerm_storage_account.storage12345_sa.name
  container_access_type = "private"

}