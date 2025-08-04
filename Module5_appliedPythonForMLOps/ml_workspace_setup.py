# Load environment variables from a .env file
from dotenv import load_dotenv
import os

# Import Azure ML core modules
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute

# Load environment variables (AZURE_TENANT_ID, AZURE_CLIENT_ID, etc.)
load_dotenv()  # Defaults to loading from a .env file in the root directory

# Authenticate using a service principal
sp_auth = ServicePrincipalAuthentication(
    tenant_id=os.getenv("AZURE_TENANT_ID"),                  # Azure AD tenant ID
    service_principal_id=os.getenv("AZURE_CLIENT_ID"),       # Client ID (App ID) of the SP
    service_principal_password=os.getenv("AZURE_CLIENT_SECRET")  # Client secret
)

# Define resource group and workspace names
RESOURCE_GROUP = "rg-mlopsclass-we-dev"
WORKSPACE_NAME = "ws-mlopsclass-we-dev"
LOCATION = "eastus"  # Change as needed

# Create or get existing Azure ML Workspace
ws = None
try:
    ws = Workspace.get(
        name=WORKSPACE_NAME,
        subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),
        resource_group=RESOURCE_GROUP,
        auth=sp_auth
    )
    print(f"Workspace '{WORKSPACE_NAME}' found.")
except Exception as e:
    print(f"Workspace '{WORKSPACE_NAME}' not found, creating a new one...")
    ws = Workspace.create(
        name=WORKSPACE_NAME,
        subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),
        resource_group=RESOURCE_GROUP,
        location=LOCATION,
        auth=sp_auth,
        exist_ok=True
    )
    ws.wait_for_completion(show_output=True)
    print(f"Workspace '{WORKSPACE_NAME}' created.")

# Define AML compute cluster configurations
aml_computes = {
    "cpu-cluster": {
        "vm_size": "STANDARD_DS3_V2",          # Valid Azure VM size, adjust as needed
        "min_nodes": 0,
        "max_nodes": 3,
        "idle_seconds_before_scaledown": 240
    }
}

# Create or get AML compute clusters
for ct_name, config in aml_computes.items():
    if ct_name not in ws.compute_targets:
        print(f"Creating compute target: {ct_name}")
        compute_config = AmlCompute.provisioning_configuration(
            vm_size=config["vm_size"],
            min_nodes=config["min_nodes"],
            max_nodes=config["max_nodes"],
            idle_seconds_before_scaledown=config["idle_seconds_before_scaledown"]
        )
        compute_target = ComputeTarget.create(ws, ct_name, compute_config)
        compute_target.wait_for_completion(show_output=True)
        print(f"Compute target '{ct_name}' created.")
    else:
        print(f"Compute target '{ct_name}' already exists.")

# ----------- CLEANUP SECTION -----------

# Delete compute clusters to stop resources and avoid costs
for ct_name in aml_computes.keys():
    if ct_name in ws.compute_targets:
        compute_target = ws.compute_targets[ct_name]
        print(f"Deleting compute target: {ct_name}...")
        compute_target.delete()
        print(f"Compute target '{ct_name}' deleted.")

# Optional: Delete the entire workspace (comment out if not wanted)
print(f"Deleting workspace '{WORKSPACE_NAME}'...")
ws.delete()
print(f"Workspace '{WORKSPACE_NAME}' deleted.")

