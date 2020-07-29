import os

class Configuration:
    def get_configuration(self):
        # authentication
        subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
        tenant_id = os.environ["AZURE_TENANT_ID"]
        client_id = os.environ["AZURE_CLIENT_ID"]
        client_secret = os.environ["AZURE_CLIENT_SECRET"]

        return  {
            "subscriptionId": subscription_id,
            "tenantId": tenant_id,
            "clientId": client_id,
            "clientSecret": client_secret,
            "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
            "resourceManagerEndpointUrl": "https://management.azure.com/",
            "activeDirectoryGraphResourceId": "https://graph.windows.net/",
            "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
            "galleryEndpointUrl": "https://gallery.azure.com/",
            "managementEndpointUrl": "https://management.core.windows.net/"
        }