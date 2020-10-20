import unittest
import swagger_client
import os

from swagger_client.rest import ApiException

from swagger_configuration import SwaggerConfiguration
from swagger_repositories import SwaggerRepositories
from swagger_storage import SwaggerStorage


class TestSwaggerNexusAPI(unittest.TestCase):
    swagger_storage = None
    swagger_repositories = None
    configuration = None

    authorization_header_value = None

    api_client = None
    docker_repo_api_client = None

    docker_blob_store = "my_docker_repo_store"
    docker_repo_name = "my_docker_repo"

    helm_blob_store = "my_helm_repo_store"
    helm_store = "my_helm_store"

    def setUp(self):
        swagger_configuration = SwaggerConfiguration()
        self.configuration = swagger_configuration.get_configuration()
        authorization_header_value = swagger_configuration.get_authorization_header()
        self.api_client = swagger_client.ApiClient(self.configuration,
                                                   header_name="Authorization",
                                                   header_value=authorization_header_value)
        self.swagger_storage = SwaggerStorage(self.api_client)
        self.swagger_repositories = SwaggerRepositories(self.api_client, self.swagger_storage)

    def test_list_blob_stores(self):
        self.swagger_storage.list_blob_stores()

    def test_delete_blob_store(self):
        self.swagger_storage.delete_blob_store(self.docker_blob_store)

    def test_create_file_blob_store(self):
        self.swagger_storage.create_blob_store(self.docker_blob_store)

    def test_list_repositories(self):
        self.swagger_repositories.list_repositories()

    def test_list_repositories_by_format_and_type(self):
        repositories = self.swagger_repositories.get_repositories("docker", "hosted")
        for repo in repositories:
            print('Your repo name is---> ', repo.name)
            print('Your repo type is---> ', repo.format)
            print('Your repo type is---> ', repo.type)
            print('Your repo url is---> ', repo.url)

    def test_delete_repository(self):
        self.swagger_repositories.delete_repository(self.docker_repo_name)

    def test_create_docker_hosted_repository(self):
        self.swagger_repositories.create_docker_hosted_repository(self.docker_repo_name)



if __name__ == '__main__':
    unittest.main()
