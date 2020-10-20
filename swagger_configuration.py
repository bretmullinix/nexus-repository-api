import os
import swagger_client
from swagger_client import Configuration

from utilities import get_base64_string


class SwaggerConfiguration:

    username = os.getenv('NEXUS_USER_NAME')
    password = os.environ.get('NEXUS_PASSWORD')
    nexus_server_url = os.getenv('NEXUS_URL')

    def __init__(self):
       pass

    def get_configuration(self):
        configuration = Configuration()
        configuration.host = self.nexus_server_url + "/service/rest"
        configuration.verify_ssl = False
        configuration.debug = True
        return configuration

    def get_authorization_header(self):
        credentials = self.username + ":" + self.password
        encoded_credentials = get_base64_string(credentials)
        result = "Basic " + encoded_credentials
        return result
