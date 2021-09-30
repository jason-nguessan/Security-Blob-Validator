
# BlobEndpoint=https://storage12345storage12345.blob.core.windows.net/;QueueEndpoint=https://storage12345storage12345.queue.core.windows.net/;FileEndpoint=https://storage12345storage12345.file.core.windows.net/;TableEndpoint=https://storage12345storage12345.table.core.windows.net/;SharedAccessSignature=sv=2020-08-04&ss=bfqt&srt=co&sp=rwdlacupitfx&se=2021-10-01T04:05:17Z&st=2021-09-30T20:05:17Z&spr=https&sig=YLSBxcVv4qviPxVcZhX9q1cQq2%2FBgHg2Z6Mw5CLvyRM%3D

# https://storage12345storage12345.blob.core.windows.net/?sv=2020-08-04&ss=bfqt&srt=co&sp=rwdlacupitfx&se=2021-10-01T04:05:17Z&st=2021-09-30T20:05:17Z&spr=https&sig=YLSBxcVv4qviPxVcZhX9q1cQq2%2FBgHg2Z6Mw5CLvyRM%3D

import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


class AzureValidator:

    def __init__(self, url, shared_access_key):

        self.url = url
        self.shared_access_key = shared_access_key
        try:
            print("Azure Blob Storage v" + __version__ +
                  " - Python quickstart sample")
            blobServiceClient = BlobServiceClient(
                self.url, credential=self.shared_access_key)

            container_client = blobServiceClient.list_containers()
            for blob in container_client:
                print(blob.name)

            # Quick start code goes here

        except Exception as ex:
            print('Exceptihon:')
            print(ex)


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


azureValidator = AzureValidator(
    "https://storage12345storage12345.blob.core.windows.net/", "?sv=2020-08-04&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2021-10-01T04:24:45Z&st=2021-09-30T20:24:45Z&spr=https,http&sig=xI%2BvVK9n%2BsyCmCho3sAfnxiWhL2XR72p8ACq7tdvpYc%3D")

# test_answer()
