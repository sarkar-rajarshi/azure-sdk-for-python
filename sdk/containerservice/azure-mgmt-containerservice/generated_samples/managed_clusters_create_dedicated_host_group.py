# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.containerservice import ContainerServiceClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-containerservice
# USAGE
    python managed_clusters_create_dedicated_host_group.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerServiceClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.managed_clusters.begin_create_or_update(
        resource_group_name="rg1",
        resource_name="clustername1",
        parameters={
            "location": "location1",
            "properties": {
                "addonProfiles": {},
                "agentPoolProfiles": [
                    {
                        "count": 3,
                        "enableNodePublicIP": True,
                        "hostGroupID": "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/rg/providers/Microsoft.Compute/hostGroups/hostgroup1",
                        "name": "nodepool1",
                        "osType": "Linux",
                        "type": "VirtualMachineScaleSets",
                        "vmSize": "Standard_DS2_v2",
                    }
                ],
                "autoScalerProfile": {"scale-down-delay-after-add": "15m", "scan-interval": "20s"},
                "diskEncryptionSetID": "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/rg1/providers/Microsoft.Compute/diskEncryptionSets/des",
                "dnsPrefix": "dnsprefix1",
                "enableRBAC": True,
                "kubernetesVersion": "",
                "linuxProfile": {"adminUsername": "azureuser", "ssh": {"publicKeys": [{"keyData": "keydata"}]}},
                "networkProfile": {
                    "loadBalancerProfile": {"managedOutboundIPs": {"count": 2}},
                    "loadBalancerSku": "standard",
                    "outboundType": "loadBalancer",
                },
                "servicePrincipalProfile": {"clientId": "clientid", "secret": "secret"},
                "windowsProfile": {"adminPassword": "replacePassword1234$", "adminUsername": "azureuser"},
            },
            "sku": {"name": "Basic", "tier": "Free"},
            "tags": {"archv2": "", "tier": "production"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/containerservice/resource-manager/Microsoft.ContainerService/aks/stable/2025-05-01/examples/ManagedClustersCreate_DedicatedHostGroup.json
if __name__ == "__main__":
    main()
