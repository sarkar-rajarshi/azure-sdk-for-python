# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.oracledatabase import OracleDatabaseMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOracleDatabaseMgmtCloudExadataInfrastructuresOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(OracleDatabaseMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_cloud_exadata_infrastructures_list_by_subscription(self, resource_group):
        response = self.client.cloud_exadata_infrastructures.list_by_subscription()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_cloud_exadata_infrastructures_begin_create_or_update(self, resource_group):
        response = self.client.cloud_exadata_infrastructures.begin_create_or_update(
            resource_group_name=resource_group.name,
            cloudexadatainfrastructurename="str",
            resource={
                "location": "str",
                "zones": ["str"],
                "id": "str",
                "name": "str",
                "properties": {
                    "displayName": "str",
                    "shape": "str",
                    "activatedStorageCount": 0,
                    "additionalStorageCount": 0,
                    "availableStorageSizeInGbs": 0,
                    "computeCount": 0,
                    "computeModel": "str",
                    "cpuCount": 0,
                    "customerContacts": [{"email": "str"}],
                    "dataStorageSizeInTbs": 0.0,
                    "databaseServerType": "str",
                    "dbNodeStorageSizeInGbs": 0,
                    "dbServerVersion": "str",
                    "definedFileSystemConfiguration": [
                        {"isBackupPartition": bool, "isResizable": bool, "minSizeGb": 0, "mountPoint": "str"}
                    ],
                    "estimatedPatchingTime": {
                        "estimatedDbServerPatchingTime": 0,
                        "estimatedNetworkSwitchesPatchingTime": 0,
                        "estimatedStorageServerPatchingTime": 0,
                        "totalEstimatedPatchingTime": 0,
                    },
                    "lastMaintenanceRunId": "str",
                    "lifecycleDetails": "str",
                    "lifecycleState": "str",
                    "maintenanceWindow": {
                        "customActionTimeoutInMins": 0,
                        "daysOfWeek": [{"name": "str"}],
                        "hoursOfDay": [0],
                        "isCustomActionTimeoutEnabled": bool,
                        "isMonthlyPatchingEnabled": bool,
                        "leadTimeInWeeks": 0,
                        "months": [{"name": "str"}],
                        "patchingMode": "str",
                        "preference": "str",
                        "weeksOfMonth": [0],
                    },
                    "maxCpuCount": 0,
                    "maxDataStorageInTbs": 0.0,
                    "maxDbNodeStorageSizeInGbs": 0,
                    "maxMemoryInGbs": 0,
                    "memorySizeInGbs": 0,
                    "monthlyDbServerVersion": "str",
                    "monthlyStorageServerVersion": "str",
                    "nextMaintenanceRunId": "str",
                    "ociUrl": "str",
                    "ocid": "str",
                    "provisioningState": "str",
                    "storageCount": 0,
                    "storageServerType": "str",
                    "storageServerVersion": "str",
                    "timeCreated": "str",
                    "totalStorageSizeInGbs": 0,
                },
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_cloud_exadata_infrastructures_get(self, resource_group):
        response = self.client.cloud_exadata_infrastructures.get(
            resource_group_name=resource_group.name,
            cloudexadatainfrastructurename="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_cloud_exadata_infrastructures_begin_update(self, resource_group):
        response = self.client.cloud_exadata_infrastructures.begin_update(
            resource_group_name=resource_group.name,
            cloudexadatainfrastructurename="str",
            properties={
                "properties": {
                    "computeCount": 0,
                    "customerContacts": [{"email": "str"}],
                    "displayName": "str",
                    "maintenanceWindow": {
                        "customActionTimeoutInMins": 0,
                        "daysOfWeek": [{"name": "str"}],
                        "hoursOfDay": [0],
                        "isCustomActionTimeoutEnabled": bool,
                        "isMonthlyPatchingEnabled": bool,
                        "leadTimeInWeeks": 0,
                        "months": [{"name": "str"}],
                        "patchingMode": "str",
                        "preference": "str",
                        "weeksOfMonth": [0],
                    },
                    "storageCount": 0,
                },
                "tags": {"str": "str"},
                "zones": ["str"],
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_cloud_exadata_infrastructures_begin_delete(self, resource_group):
        response = self.client.cloud_exadata_infrastructures.begin_delete(
            resource_group_name=resource_group.name,
            cloudexadatainfrastructurename="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_cloud_exadata_infrastructures_list_by_resource_group(self, resource_group):
        response = self.client.cloud_exadata_infrastructures.list_by_resource_group(
            resource_group_name=resource_group.name,
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_cloud_exadata_infrastructures_begin_add_storage_capacity(self, resource_group):
        response = self.client.cloud_exadata_infrastructures.begin_add_storage_capacity(
            resource_group_name=resource_group.name,
            cloudexadatainfrastructurename="str",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
