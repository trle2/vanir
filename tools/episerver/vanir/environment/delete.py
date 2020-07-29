from episerver.vanir.configuration import Configuration
from azure.common.client_factory import get_client_from_json_dict
from azure.mgmt.resource import ResourceManagementClient

class DeleteEnvironmentCommand:
    def __init__(self, env_name):
        config = Configuration()
        self.env_name = env_name
        self.resource_client = get_client_from_json_dict(ResourceManagementClient, config.get_configuration())
        
    def execute(self):
        self.resource_client.resource_groups.delete(self.env_name)