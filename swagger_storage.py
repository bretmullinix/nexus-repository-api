import swagger_client
from swagger_client import FileBlobStoreApiCreateRequest


class SwaggerStorage:
    api_client = None

    def __init__(self, api_client: swagger_client.api_client):
        self.api_client = api_client

    def list_blob_stores(self):
        blob_store_api = swagger_client.BlobStoreApi(self.api_client)
        blob_store_name = "default"
        blob_stores = blob_store_api.list_blob_stores()

        for blob_store in blob_stores:
            print('Your blob store name is---> ', blob_store.name)
            print('Your blob store type is--->', blob_store.type)
            print('Your blob count is-->', str(blob_store.blob_count))
            print('Your blob store total size in bytes--->', str(blob_store.total_size_in_bytes))
            print('Your blob store available size in bytes--->', str(blob_store.available_space_in_bytes))
            print(type(blob_store))

    def is_blob_store(self, name):
        blob_store_api = swagger_client.BlobStoreApi(self.api_client)
        blob_store_name = "default"
        blob_stores = blob_store_api.list_blob_stores()
        for blob_store in blob_stores:
            if blob_store.name == name:
                return True
        return False

    def delete_blob_store(self, name):
        if not self.is_blob_store(name):
            return
        blob_store_api = swagger_client.BlobStoreApi(self.api_client)
        blob_store_api.delete_blob_store(name)

    def create_blob_store(self, blob_store_name):
        if self.is_blob_store(blob_store_name):
            return
        blob_store_api = swagger_client.BlobStoreApi(self.api_client)
        request = FileBlobStoreApiCreateRequest(path=blob_store_name, name=blob_store_name)
        blob_store_api.create_file_blob_store(body=request)