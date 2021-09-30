
# BlobEndpoint=https://storage12345storage12345.blob.core.windows.net/;QueueEndpoint=https://storage12345storage12345.queue.core.windows.net/;FileEndpoint=https://storage12345storage12345.file.core.windows.net/;TableEndpoint=https://storage12345storage12345.table.core.windows.net/;SharedAccessSignature=sv=2020-08-04&ss=bfqt&srt=co&sp=rwdlacupitfx&se=2021-10-01T04:05:17Z&st=2021-09-30T20:05:17Z&spr=https&sig=YLSBxcVv4qviPxVcZhX9q1cQq2%2FBgHg2Z6Mw5CLvyRM%3D

# https://storage12345storage12345.blob.core.windows.net/?sv=2020-08-04&ss=bfqt&srt=co&sp=rwdlacupitfx&se=2021-10-01T04:05:17Z&st=2021-09-30T20:05:17Z&spr=https&sig=YLSBxcVv4qviPxVcZhX9q1cQq2%2FBgHg2Z6Mw5CLvyRM%3D

from azure.storage.blob import BlobServiceClient
import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


# sudo -s pip3.9 install azure.storage.blob

# pip3.9 install azure-keyvault-secrets

# pip3.9 install azure-identity

# az login

# replace kVUri with the uri of your keyvault

# replace the sas url, and token with your own
class AzureValidator:

    def __init__(self, storageAccountUrl, sharedAccessKey, kvUrl, secretPassword):

        # BEST TO EXPORT TO PATH os.environ["KEY_VAULT_NAME"]

        self._connectToClients(storageAccountUrl, sharedAccessKey, kvUrl)
        if(not self.blobServiceClient or not self.keyVaultClient):
            return

        print(self.keyVaultClient.get_secret(secretPassword).value)

    def _connectToClients(self, storageAccountUrl, sharedAccessKey, kvUrl):
        print("")

        try:
            self.keyVaultClient = SecretClient(
                vault_url=kvUrl, credential=DefaultAzureCredential())
            self.blobServiceClient = BlobServiceClient(
                storageAccountUrl, credential=sharedAccessKey)
            print("----------\n Successfully Signed in \n----------")
        except Exception as ex:
            print(ex)
            self.keyVaultClient = None
            self.blobServiceClient = None

    def _checkBlobName(self) -> bool:
        container_client = self.blobServiceClient.list_containers()
        for blob in container_client:
            print(blob.name)


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


azureValidator = AzureValidator(
    "https://storage12345storage12345.blob.core.windows.net/",
    "?sv=2020-08-04&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2021-10-01T04:24:45Z&st=2021-09-30T20:24:45Z&spr=https,http&sig=xI%2BvVK9n%2BsyCmCho3sAfnxiWhL2XR72p8ACq7tdvpYc%3D",
    f"https://pytestkeyvault.vault.azure.net",
    "secretPassword"
)

# test_answer()


# connection_string = ''
# blob_service_client = BlobServiceClient.from_connection_string(
#     connection_string)
# container_client = blob_service_client.get_container_client("<container name>")
# blob_client = container_client.get_blob_client("<blob name>")
# blob_client.download_blob().readall()  # read blob content as string
