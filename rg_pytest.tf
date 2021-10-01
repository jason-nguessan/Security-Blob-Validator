
data "azurerm_client_config" "current" {}


#Pytest Resource Group
resource "azurerm_resource_group" "pytest_rg" {
  name     = "pytest"
  location = "Canada Central"
}



#STEP 1 
  # Uncomment the following and create a key vault
  
  # Once done, comment it or delete it
  

/*

#Pytest Keyvault

# Create your Key vault and assign a password
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

#Please create your secret outside of terraform or do it here (not - recommended)

*/

#Step 2 - Uncomment the rest

/*

variable nContainers {
  type        = number
  default     = 1500
  description = "This creates N numbers of containers - USE AT YOUR OWN RISK"
}



#Pytestkeyvault
data "azurerm_key_vault" "pytest_kv" {
  name = "pytestKeyVault"
  resource_group_name = azurerm_resource_group.pytest_rg.name
}


#Pytest vault secret
data "azurerm_key_vault_secret" "secretPassword1" {
  name         = "secretPassword1"
  key_vault_id =  data.azurerm_key_vault.pytest_kv.id
}


#pytest storage account 
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


#pytest storage container



resource "azurerm_storage_container" "storage1_container" {
  count                 = var.nContainers
  name                  =  count.index % 5 == 0  ?"file${count.index}" : lower("${data.azurerm_key_vault_secret.secretPassword1.value}${count.index}")
  storage_account_name  = azurerm_storage_account.storage12345_sa.name
  container_access_type = "private"

}

*/