import unittest
import swagger_client
import base64
from swagger_client import Configuration, FileBlobStoreApiCreateRequest, FileBlobStoreApiModel, \
    GenericBlobStoreApiResponse, DockerHostedApiRepository, DockerHostedRepositoryApiRequest, DockerAttributes, \
    HostedStorageAttributes
from swagger_client.rest import ApiException


class TestSwaggerNexusAPI(unittest.TestCase):

    @staticmethod
    def get_base64_string(value):
        value_bytes = value.encode('ascii')
        base64_bytes = base64.b64encode(value_bytes)
        base64_value = base64_bytes.decode('ascii')
        return base64_value

    configuration = None
    authorization_header_value = None
    username = "<your user name>"
    password = "<your password>"
    encoded_credentials = None
    api_client = None
    docker_repo_api_client = None
    docker_blob_store = "my_docker_repo_store"
    docker_repo_name = "my_docker_repo"
    def setUp(self):
        self.configuration = Configuration()
        self.configuration.host = "https://nexus.example.com:8443/service/rest"
        self.configuration.verify_ssl = False
        self.configuration.debug = True

        credentials = self.username + ":" + self.password
        self.encoded_credentials = TestSwaggerNexusAPI.get_base64_string(credentials)
        self.authorization_header_value = "Basic " + self.encoded_credentials
        self.api_client = swagger_client.ApiClient(self.configuration,
                                              header_name="Authorization",
                                              header_value=self.authorization_header_value)


    def test_list_blob_stores(self):

        blob_store_api = swagger_client.BlobStoreApi(self.api_client)
        blob_store_name = "default"
        blob_stores = blob_store_api.list_blob_stores()

        for blob_store in blob_stores:
            print('Your blob store name is---> ', blob_store.name)
            print('Your blob store type is--->', blob_store.type)
            print('Your blob count is-->', str(blob_store.blob_count))
            print('Your blob store total size in bytes--->' , str(blob_store.total_size_in_bytes))
            print('Your blob store available size in bytes--->' , str(blob_store.available_space_in_bytes))
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

    def test_delete_blob_store(self):
        self.delete_blob_store(self.docker_blob_store)

    def test_create_file_blob_store(self):


        self.delete_blob_store(self.docker_blob_store)

        blob_store_api = swagger_client.BlobStoreApi(self.api_client)

        request = FileBlobStoreApiCreateRequest(path=self.docker_blob_store, name=self.docker_blob_store)
        blob_store_api.create_file_blob_store(body=request)


    def test_create_docker_hosted_repository(self):

        self.repository_api = swagger_client.RepositoryManagementApi(self.api_client)
        docker_attributes = DockerAttributes(https_port=8085,
                                             force_basic_auth=True,
                                             v1_enabled=True)

        docker_blob_store_attributes = HostedStorageAttributes(
                                                               blob_store_name=self.docker_blob_store,
                                                               strict_content_type_validation=True,
                                                               write_policy="allow_once"
                                                               )

        request = DockerHostedRepositoryApiRequest(name=self.docker_repo_name,
                                                   storage=docker_blob_store_attributes,
                                                   online=True,
                                                   cleanup=None,
                                                   docker = docker_attributes)


        self.repository_api.create_repository35(body=request) # Swagger doesn't define a good name for creating docker
                                                              # repositories



if __name__ == '__main__':
    unittest.main()

