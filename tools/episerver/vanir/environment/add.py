from episerver.vanir.configuration import Configuration
from azure.common.client_factory import get_client_from_json_dict
from azure.mgmt.resource import ResourceManagementClient

class AddEnvironmentCommand:
    def __init__(self):
        config = Configuration()
        self.resource_client = get_client_from_json_dict(ResourceManagementClient, config.get_configuration())
        
    def execute(self, args):
        resource_group = self.resource_client.resource_groups.create_or_update(args.name, { "location": f"{args.location}" })
        print(f"Provisioned resource group {resource_group.name} in the {resource_group.location} region")