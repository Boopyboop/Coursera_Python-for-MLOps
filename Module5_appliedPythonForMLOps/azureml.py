# Load environment variables from a .env file
from dotenv import load_dotenv
import os

# Import Azure ML core modules
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core import Workspace

# Load environment variables (AZURE_TENANT_ID, AZURE_CLIENT_ID, etc.)
load_dotenv()  # Defaults to loading from a .env file in the root directory

# Authenticate using a service principal
sp_auth = ServicePrincipalAuthentication(
    tenant_id=os.getenv("AZURE_TENANT_ID"),                  # Azure AD tenant ID
    service_principal_id=os.getenv("AZURE_CLIENT_ID"),       # Client ID (App ID) of the SP
    service_principal_password=os.getenv("AZURE_CLIENT_SECRET")  # Client secret
)

# Connect to an existing Azure ML Workspace
ws = Workspace.get(
    name="ws-mlopsclass-we-dev",                             # Name of the Azure ML workspace
    subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),      # Subscription ID from Azure
    resource_group="rg-mlopsclass-we-dev",                   # Name of the resource group
    auth=sp_auth                                              # Authenticated via SP credentials
)
