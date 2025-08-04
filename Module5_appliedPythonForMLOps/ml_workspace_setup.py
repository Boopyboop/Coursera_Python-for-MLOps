# Load environment variables from a .env file
from dotenv import load_dotenv
import os

# Import Azure ML core modules
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core import Workspace
from azureml.exceptions import ProjectSystemException

# Load environment variables (AZURE_TENANT_ID, AZURE_CLIENT_ID, etc.)
load_dotenv()

# Authenticate using a service principal
sp_auth = ServicePrincipalAuthentication(
    tenant_id=os.getenv("AZURE_TENANT_ID"),                      # Azure AD tenant ID
    service_principal_id=os.getenv("AZURE_CLIENT_ID"),           # Client ID (App ID) of the SP
    service_principal_password=os.getenv("AZURE_CLIENT_SECRET")  # Client secret
)

# Define configuration variables
SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")
RESOURCE_GROUP = "rg-mlopsclass-we-dev"
WORKSPACE_NAME = "ws-mlopsclass-we-dev"
LOCATION = "westeurope"  # Choose your preferred Azure region

# Try to load the workspace; if not found, create it
try:
    ws = Workspace.get(
        name=WORKSPACE_NAME,
        subscription_id=SUBSCRIPTION_ID,
        resource_group=RESOURCE_GROUP,
        auth=sp_auth
    )
    print(f"✅ Loaded existing workspace: {WORKSPACE_NAME}")
except Exception as e:
    print(f"⚠️ Workspace not found. Creating a new one in resource group: {RESOURCE_GROUP}")
    ws = Workspace.create(
        name=WORKSPACE_NAME,
        subscription_id=SUBSCRIPTION_ID,
        resource_group=RESOURCE_GROUP,
        location=LOCATION,
        auth=sp_auth,
        exist_ok=True,
        show_output=True
    )

# Optionally save workspace config for reuse
ws.write_config(path=".azureml")
print("✅ Workspace configuration saved to .azureml/config.json")
