import swagger_client
from swagger_client import FileBlobStoreApiCreateRequest, HostedStorageAttributes, DockerHostedRepositoryApiRequest
from swagger_client import DockerAttributes

from swagger_storage import SwaggerStorage


class SwaggerRepositories:
    api_client = None
    swagger_storage = None

    def __init__(self,  api_client: swagger_client.api_client, swagger_storage: SwaggerStorage):
        self.api_client = api_client
        self.swagger_storage = swagger_storage

    def list_repositories(self):
        repository_api = swagger_client.RepositoriesApi(self.api_client)
        repositories = repository_api.get_repositories1()

        for repo in repositories:
            print('Your repo name is---> ', repo.name)
            print('Your repo type is---> ', repo.format)
            print('Your repo type is---> ', repo.type)
            print('Your repo url is---> ', repo.url)

    def get_all_repositories(self):
        repository_api = swagger_client.RepositoriesApi(self.api_client)
        results = repository_api.get_repositories1()
        return results

    def get_repositories(self, repo_format, repo_type):
        repositories = self.get_all_repositories()
        if len(repositories) == 0:
            return []
        filtered_list = [x for x in repositories if x.format == repo_format and x.type == repo_type]
        return filtered_list

    def get_repository(self, repo_name):
        repositories = self.get_all_repositories()
        if len(repositories) == 0:
            return []
        filtered_list = [x for x in repositories if x.name == repo_name]
        if len(filtered_list) == 0:
            return None
        return filtered_list[0]

    def is_repo(self, name):
        repository = self.get_repository(name)
        if repository:
            return True
        else:
            return False

    def delete_repository(self, name):
        if not self.is_repo(name):
            return;
        repository_api = swagger_client.RepositoryManagementApi(self.api_client)
        repository_api.delete_repository(name)

    def create_docker_hosted_repository(self, name):
        self.delete_repository(name)
        self.swagger_storage.create_blob_store(name)
        repository_api = swagger_client.RepositoryManagementApi(self.api_client)
        docker_attributes = DockerAttributes(https_port=8085,
                                             force_basic_auth=True,
                                             v1_enabled=True)

        docker_blob_store_attributes = HostedStorageAttributes(
            blob_store_name=name,
            strict_content_type_validation=True,
            write_policy="allow_once"
        )

        request = DockerHostedRepositoryApiRequest(name=name,
                                                   storage=docker_blob_store_attributes,
                                                   online=True,
                                                   cleanup=None,
                                                   docker=docker_attributes)

        repository_api.create_repository35(body=request)  # Swagger doesn't define a good name for creating docker
        # repositories
