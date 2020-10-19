import unittest
import swagger_client
import base64
import os
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
    username = os.getenv('NEXUS_USER_NAME')
    password = os.environ.get('NEXUS_PASSWORD')
    nexus_server_url = os.getenv('NEXUS_URL')
    encoded_credentials = None
    api_client = None
    docker_repo_api_client = None
    docker_blob_store = "my_docker_repo_store"
    docker_repo_name = "my_docker_repo"

    def setUp(self):
        self.configuration = Configuration()
        self.configuration.host = self.nexus_server_url + "/service/rest"
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

    def test_delete_blob_store(self):
        self.delete_blob_store(self.docker_blob_store)

    def test_create_file_blob_store(self):
        self.create_blob_store()

    def create_blob_store(self):
        self.delete_blob_store(self.docker_blob_store)
        blob_store_api = swagger_client.BlobStoreApi(self.api_client)
        request = FileBlobStoreApiCreateRequest(path=self.docker_blob_store, name=self.docker_blob_store)
        blob_store_api.create_file_blob_store(body=request)

    def test_list_repositories(self):

        self.repository_api = swagger_client.RepositoriesApi(self.api_client)
        repositories = self.repository_api.get_repositories1()

        for repo in repositories:
            print('Your repo name is---> ', repo.name)
            print('Your repo type is---> ', repo.format)
            print('Your repo type is---> ', repo.type)
            print('Your repo url is---> ', repo.url)

    def get_repositories(self, repo_format, repo_type):
        self.repository_api = swagger_client.RepositoriesApi(self.api_client)
        repositories = self.repository_api.get_repositories1()
        if len(repositories) == 0:
            return []
        filtered_list = [ x for x in repositories if x.format == repo_format and x.type == repo_type ]
        return filtered_list

    def test_list_repositories_by_format_and_type(self):

        repositories = self.get_repositories("docker", "hosted")
        for repo in repositories:
            print('Your repo name is---> ', repo.name)
            print('Your repo type is---> ', repo.format)
            print('Your repo type is---> ', repo.type)
            print('Your repo url is---> ', repo.url)

    def test_create_docker_hosted_repository(self):
        self.create_blob_store()
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
                                                   docker=docker_attributes)

        self.repository_api.create_repository35(body=request)  # Swagger doesn't define a good name for creating docker
        # repositories


if __name__ == '__main__':
    unittest.main()
