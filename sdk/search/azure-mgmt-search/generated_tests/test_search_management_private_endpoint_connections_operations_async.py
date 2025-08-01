# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.search.aio import SearchManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSearchManagementPrivateEndpointConnectionsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SearchManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_private_endpoint_connections_update(self, resource_group):
        response = await self.client.private_endpoint_connections.update(
            resource_group_name=resource_group.name,
            search_service_name="str",
            private_endpoint_connection_name="str",
            private_endpoint_connection={
                "id": "str",
                "name": "str",
                "properties": {
                    "groupId": "str",
                    "privateEndpoint": {"id": "str"},
                    "privateLinkServiceConnectionState": {
                        "actionsRequired": "None",
                        "description": "str",
                        "status": "str",
                    },
                    "provisioningState": "str",
                },
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
            api_version="2025-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_private_endpoint_connections_get(self, resource_group):
        response = await self.client.private_endpoint_connections.get(
            resource_group_name=resource_group.name,
            search_service_name="str",
            private_endpoint_connection_name="str",
            api_version="2025-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_private_endpoint_connections_delete(self, resource_group):
        response = await self.client.private_endpoint_connections.delete(
            resource_group_name=resource_group.name,
            search_service_name="str",
            private_endpoint_connection_name="str",
            api_version="2025-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_private_endpoint_connections_list_by_service(self, resource_group):
        response = self.client.private_endpoint_connections.list_by_service(
            resource_group_name=resource_group.name,
            search_service_name="str",
            api_version="2025-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
