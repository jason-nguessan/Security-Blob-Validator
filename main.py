from azure.storage.blob import BlobServiceClient
import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


class AzureSecretValidator:

    def __init__(self, storageAccountUrl, sharedAccessKey, kvUrl, secretName):

        # BEST TO EXPORT TO PATH os.environ["KEY_VAULT_NAME"]

        self._connectToClients(storageAccountUrl, sharedAccessKey, kvUrl)
        if(not self.blobServiceClient or not self.keyVaultClient):
            return

        self.secret = self.keyVaultClient.get_secret(secretName).value

    def _connectToClients(self, storageAccountUrl, sharedAccessKey, kvUrl):

        try:
            self.keyVaultClient = SecretClient(
                vault_url=kvUrl, credential=DefaultAzureCredential())
            self.blobServiceClient = BlobServiceClient(
                storageAccountUrl, credential=sharedAccessKey)
            print("----------\n Successfully Signed in \n----------")
            print(
                "----------\n Throws Warning if Keyvault is not exported to OS \n----------")
        except Exception as ex:
            print(ex)
            self.keyVaultClient = None
            self.blobServiceClient = None

    def isSecretInBlobName(self) -> bool:
        for blob in self.blobServiceClient.list_containers():
            if(self.secret in blob.name):
                print(
                    "----------\n Breach!!!! Secret was Found in Container's Name \n----------")
                return True
        return False


# STEP 1 - Run these commands in super use mode before running these commands  - python 3.9.7

        # az login

        # pip3.9 install azure.storage.blob

        # pip3.9 install azure-keyvault-secrets

        # pip3.9 install azure-identity

        # pip3.9 install pytest


# STEP 2 - Replace the following values with your own  - Valid untill 01/01/2022

# storage account url
storageAccountUrl = "https://storage12345storage12345.blob.core.windows.net/"

# shared access key, also known as shared access token
sharedAccessKey = "?sv=2020-08-04&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2021-10-16T00:44:05Z&st=2021-10-01T16:44:05Z&spr=https&sig=y3TJpZOx%2BVOz6xNLuBG7p%2BONIWcSBx4C1BO5M8G9LA0%3D"


# key vault url
kvUrl = f"https://pytestkeyvault.vault.azure.net"

# key vault secret name
secretName = "secretPassword1"


# STEP 3 - Run the command

# python3.9 main.py

azureValidator = AzureSecretValidator(
    storageAccountUrl, sharedAccessKey, kvUrl, secretName)


assert(azureValidator.isSecretInBlobName() == False)


