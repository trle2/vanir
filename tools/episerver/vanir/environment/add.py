from episerver.vanir.configuration import Configuration
from azure.common.client_factory import get_client_from_json_dict
from azure.mgmt.resource import ResourceManagementClient

class AddEnvironmentCommand:
    def __init__(self, env_name, env_location):
        config = Configuration()
        self.env_name = env_name
        self.env_location = env_location
        self.resource_client = get_client_from_json_dict(ResourceManagementClient, config.get_configuration())
        
    def execute(self):
        resource_group = self.resource_client.resource_groups.create_or_update(self.env_name, { "location": f"{self.env_location}" })
        print(f"Provisioned resource group {resource_group.name} in the {resource_group.location} region")