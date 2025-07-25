# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.policyinsights import PolicyInsightsClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPolicyInsightsRemediationsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(PolicyInsightsClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_list_deployments_at_management_group(self, resource_group):
        response = self.client.remediations.list_deployments_at_management_group(
            management_group_id="str",
            remediation_name="str",
            management_groups_namespace="Microsoft.Management",
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_cancel_at_management_group(self, resource_group):
        response = self.client.remediations.cancel_at_management_group(
            management_group_id="str",
            remediation_name="str",
            management_groups_namespace="Microsoft.Management",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_list_for_management_group(self, resource_group):
        response = self.client.remediations.list_for_management_group(
            management_group_id="str",
            management_groups_namespace="Microsoft.Management",
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_create_or_update_at_management_group(self, resource_group):
        response = self.client.remediations.create_or_update_at_management_group(
            management_group_id="str",
            remediation_name="str",
            parameters={
                "correlationId": "str",
                "createdOn": "2020-02-20 00:00:00",
                "deploymentStatus": {"failedDeployments": 0, "successfulDeployments": 0, "totalDeployments": 0},
                "failureThreshold": {"percentage": 0.0},
                "filters": {"locations": ["str"], "resourceIds": ["str"]},
                "id": "str",
                "lastUpdatedOn": "2020-02-20 00:00:00",
                "name": "str",
                "parallelDeployments": 0,
                "policyAssignmentId": "str",
                "policyDefinitionReferenceId": "str",
                "provisioningState": "str",
                "resourceCount": 0,
                "resourceDiscoveryMode": "str",
                "statusMessage": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            management_groups_namespace="Microsoft.Management",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_get_at_management_group(self, resource_group):
        response = self.client.remediations.get_at_management_group(
            management_group_id="str",
            remediation_name="str",
            management_groups_namespace="Microsoft.Management",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_delete_at_management_group(self, resource_group):
        response = self.client.remediations.delete_at_management_group(
            management_group_id="str",
            remediation_name="str",
            management_groups_namespace="Microsoft.Management",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_list_deployments_at_subscription(self, resource_group):
        response = self.client.remediations.list_deployments_at_subscription(
            remediation_name="str",
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_cancel_at_subscription(self, resource_group):
        response = self.client.remediations.cancel_at_subscription(
            remediation_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_list_for_subscription(self, resource_group):
        response = self.client.remediations.list_for_subscription(
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_create_or_update_at_subscription(self, resource_group):
        response = self.client.remediations.create_or_update_at_subscription(
            remediation_name="str",
            parameters={
                "correlationId": "str",
                "createdOn": "2020-02-20 00:00:00",
                "deploymentStatus": {"failedDeployments": 0, "successfulDeployments": 0, "totalDeployments": 0},
                "failureThreshold": {"percentage": 0.0},
                "filters": {"locations": ["str"], "resourceIds": ["str"]},
                "id": "str",
                "lastUpdatedOn": "2020-02-20 00:00:00",
                "name": "str",
                "parallelDeployments": 0,
                "policyAssignmentId": "str",
                "policyDefinitionReferenceId": "str",
                "provisioningState": "str",
                "resourceCount": 0,
                "resourceDiscoveryMode": "str",
                "statusMessage": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_get_at_subscription(self, resource_group):
        response = self.client.remediations.get_at_subscription(
            remediation_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_delete_at_subscription(self, resource_group):
        response = self.client.remediations.delete_at_subscription(
            remediation_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_list_deployments_at_resource_group(self, resource_group):
        response = self.client.remediations.list_deployments_at_resource_group(
            resource_group_name=resource_group.name,
            remediation_name="str",
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_cancel_at_resource_group(self, resource_group):
        response = self.client.remediations.cancel_at_resource_group(
            resource_group_name=resource_group.name,
            remediation_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_list_for_resource_group(self, resource_group):
        response = self.client.remediations.list_for_resource_group(
            resource_group_name=resource_group.name,
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_create_or_update_at_resource_group(self, resource_group):
        response = self.client.remediations.create_or_update_at_resource_group(
            resource_group_name=resource_group.name,
            remediation_name="str",
            parameters={
                "correlationId": "str",
                "createdOn": "2020-02-20 00:00:00",
                "deploymentStatus": {"failedDeployments": 0, "successfulDeployments": 0, "totalDeployments": 0},
                "failureThreshold": {"percentage": 0.0},
                "filters": {"locations": ["str"], "resourceIds": ["str"]},
                "id": "str",
                "lastUpdatedOn": "2020-02-20 00:00:00",
                "name": "str",
                "parallelDeployments": 0,
                "policyAssignmentId": "str",
                "policyDefinitionReferenceId": "str",
                "provisioningState": "str",
                "resourceCount": 0,
                "resourceDiscoveryMode": "str",
                "statusMessage": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_get_at_resource_group(self, resource_group):
        response = self.client.remediations.get_at_resource_group(
            resource_group_name=resource_group.name,
            remediation_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_delete_at_resource_group(self, resource_group):
        response = self.client.remediations.delete_at_resource_group(
            resource_group_name=resource_group.name,
            remediation_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_list_deployments_at_resource(self, resource_group):
        response = self.client.remediations.list_deployments_at_resource(
            resource_id="str",
            remediation_name="str",
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_cancel_at_resource(self, resource_group):
        response = self.client.remediations.cancel_at_resource(
            resource_id="str",
            remediation_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_list_for_resource(self, resource_group):
        response = self.client.remediations.list_for_resource(
            resource_id="str",
            api_version="2024-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_create_or_update_at_resource(self, resource_group):
        response = self.client.remediations.create_or_update_at_resource(
            resource_id="str",
            remediation_name="str",
            parameters={
                "correlationId": "str",
                "createdOn": "2020-02-20 00:00:00",
                "deploymentStatus": {"failedDeployments": 0, "successfulDeployments": 0, "totalDeployments": 0},
                "failureThreshold": {"percentage": 0.0},
                "filters": {"locations": ["str"], "resourceIds": ["str"]},
                "id": "str",
                "lastUpdatedOn": "2020-02-20 00:00:00",
                "name": "str",
                "parallelDeployments": 0,
                "policyAssignmentId": "str",
                "policyDefinitionReferenceId": "str",
                "provisioningState": "str",
                "resourceCount": 0,
                "resourceDiscoveryMode": "str",
                "statusMessage": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_get_at_resource(self, resource_group):
        response = self.client.remediations.get_at_resource(
            resource_id="str",
            remediation_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_remediations_delete_at_resource(self, resource_group):
        response = self.client.remediations.delete_at_resource(
            resource_id="str",
            remediation_name="str",
            api_version="2024-10-01",
        )

        # please add some check logic here by yourself
        # ...
