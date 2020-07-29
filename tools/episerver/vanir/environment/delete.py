from episerver.vanir.configuration import Configuration
from azure.common.client_factory import get_client_from_json_dict
from azure.mgmt.resource import ResourceManagementClient

class DeleteEnvironmentCommand:
    def __init__(self):
        config = Configuration()
        self.resource_client = get_client_from_json_dict(ResourceManagementClient, config.get_configuration())
        
    def execute(self, args):
        self.resource_client.resource_groups.delete(args.name)