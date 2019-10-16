# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ProxyResource(Model):
    """Common properties of proxy resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(ProxyResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)


class DataSource(ProxyResource):
    """Datasources under OMS Workspace.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param properties: Required. The data source properties in raw json
     format, each kind of data source have it's own schema.
    :type properties: object
    :param e_tag: The ETag of the data source.
    :type e_tag: str
    :param kind: Required. Possible values include: 'AzureActivityLog',
     'ChangeTrackingPath', 'ChangeTrackingDefaultPath',
     'ChangeTrackingDefaultRegistry', 'ChangeTrackingCustomRegistry',
     'CustomLog', 'CustomLogCollection', 'GenericDataSource', 'IISLogs',
     'LinuxPerformanceObject', 'LinuxPerformanceCollection', 'LinuxSyslog',
     'LinuxSyslogCollection', 'WindowsEvent', 'WindowsPerformanceCounter'
    :type kind: str or ~azure.mgmt.loganalytics.models.DataSourceKind
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'properties': {'required': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'object'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataSource, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)
        self.e_tag = kwargs.get('e_tag', None)
        self.kind = kwargs.get('kind', None)


class DataSourceFilter(Model):
    """DataSource filter. Right now, only filter by kind is supported.

    :param kind: Possible values include: 'AzureActivityLog',
     'ChangeTrackingPath', 'ChangeTrackingDefaultPath',
     'ChangeTrackingDefaultRegistry', 'ChangeTrackingCustomRegistry',
     'CustomLog', 'CustomLogCollection', 'GenericDataSource', 'IISLogs',
     'LinuxPerformanceObject', 'LinuxPerformanceCollection', 'LinuxSyslog',
     'LinuxSyslogCollection', 'WindowsEvent', 'WindowsPerformanceCounter'
    :type kind: str or ~azure.mgmt.loganalytics.models.DataSourceKind
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataSourceFilter, self).__init__(**kwargs)
        self.kind = kwargs.get('kind', None)


class IntelligencePack(Model):
    """Intelligence Pack containing a string name and boolean indicating if it's
    enabled.

    :param name: The name of the intelligence pack.
    :type name: str
    :param enabled: The enabled boolean for the intelligence pack.
    :type enabled: bool
    :param display_name: The display name of the intelligence pack.
    :type display_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IntelligencePack, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.enabled = kwargs.get('enabled', None)
        self.display_name = kwargs.get('display_name', None)


class LinkedService(ProxyResource):
    """The top level Linked service resource container.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param resource_id: Required. The resource ID of the resource that will be
     linked to the workspace.
    :type resource_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource_id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LinkedService, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)


class ManagementGroup(Model):
    """A management group that is connected to a workspace.

    :param server_count: The number of servers connected to the management
     group.
    :type server_count: int
    :param is_gateway: Gets or sets a value indicating whether the management
     group is a gateway.
    :type is_gateway: bool
    :param name: The name of the management group.
    :type name: str
    :param id: The unique ID of the management group.
    :type id: str
    :param created: The datetime that the management group was created.
    :type created: datetime
    :param data_received: The last datetime that the management group received
     data.
    :type data_received: datetime
    :param version: The version of System Center that is managing the
     management group.
    :type version: str
    :param sku: The SKU of System Center that is managing the management
     group.
    :type sku: str
    """

    _attribute_map = {
        'server_count': {'key': 'properties.serverCount', 'type': 'int'},
        'is_gateway': {'key': 'properties.isGateway', 'type': 'bool'},
        'name': {'key': 'properties.name', 'type': 'str'},
        'id': {'key': 'properties.id', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'data_received': {'key': 'properties.dataReceived', 'type': 'iso-8601'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ManagementGroup, self).__init__(**kwargs)
        self.server_count = kwargs.get('server_count', None)
        self.is_gateway = kwargs.get('is_gateway', None)
        self.name = kwargs.get('name', None)
        self.id = kwargs.get('id', None)
        self.created = kwargs.get('created', None)
        self.data_received = kwargs.get('data_received', None)
        self.version = kwargs.get('version', None)
        self.sku = kwargs.get('sku', None)


class MetricName(Model):
    """The name of a metric.

    :param value: The system name of the metric.
    :type value: str
    :param localized_value: The localized name of the metric.
    :type localized_value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MetricName, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.localized_value = kwargs.get('localized_value', None)


class Operation(Model):
    """Supported operation of OperationalInsights resource provider.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display: ~azure.mgmt.loganalytics.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OperationDisplay(Model):
    """Display metadata associated with the operation.

    :param provider: Service provider: Microsoft OperationsManagement.
    :type provider: str
    :param resource: Resource on which the operation is performed etc.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)


class Resource(Model):
    """The resource definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class SharedKeys(Model):
    """The shared keys for a workspace.

    :param primary_shared_key: The primary shared key of a workspace.
    :type primary_shared_key: str
    :param secondary_shared_key: The secondary shared key of a workspace.
    :type secondary_shared_key: str
    """

    _attribute_map = {
        'primary_shared_key': {'key': 'primarySharedKey', 'type': 'str'},
        'secondary_shared_key': {'key': 'secondarySharedKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SharedKeys, self).__init__(**kwargs)
        self.primary_shared_key = kwargs.get('primary_shared_key', None)
        self.secondary_shared_key = kwargs.get('secondary_shared_key', None)


class Sku(Model):
    """The SKU (tier) of a workspace.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU. Possible values include:
     'Free', 'Standard', 'Premium', 'PerNode', 'PerGB2018', 'Standalone'
    :type name: str or ~azure.mgmt.loganalytics.models.SkuNameEnum
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Sku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)


class Table(Model):
    """Workspace data table definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Table ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :param retention_in_days: The table data retention in days, between 30 and
     730. Setting this property to null will default to the workspace
     retention.
    :type retention_in_days: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'retention_in_days': {'maximum': 730, 'minimum': 30},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'retention_in_days': {'key': 'properties.retentionInDays', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.retention_in_days = kwargs.get('retention_in_days', None)


class UsageMetric(Model):
    """A metric describing the usage of a resource.

    :param name: The name of the metric.
    :type name: ~azure.mgmt.loganalytics.models.MetricName
    :param unit: The units used for the metric.
    :type unit: str
    :param current_value: The current value of the metric.
    :type current_value: float
    :param limit: The quota limit for the metric.
    :type limit: float
    :param next_reset_time: The time that the metric's value will reset.
    :type next_reset_time: datetime
    :param quota_period: The quota period that determines the length of time
     between value resets.
    :type quota_period: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'MetricName'},
        'unit': {'key': 'unit', 'type': 'str'},
        'current_value': {'key': 'currentValue', 'type': 'float'},
        'limit': {'key': 'limit', 'type': 'float'},
        'next_reset_time': {'key': 'nextResetTime', 'type': 'iso-8601'},
        'quota_period': {'key': 'quotaPeriod', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UsageMetric, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.unit = kwargs.get('unit', None)
        self.current_value = kwargs.get('current_value', None)
        self.limit = kwargs.get('limit', None)
        self.next_reset_time = kwargs.get('next_reset_time', None)
        self.quota_period = kwargs.get('quota_period', None)


class Workspace(Resource):
    """The top level Workspace resource container.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param provisioning_state: The provisioning state of the workspace.
     Possible values include: 'Creating', 'Succeeded', 'Failed', 'Canceled',
     'Deleting', 'ProvisioningAccount'
    :type provisioning_state: str or
     ~azure.mgmt.loganalytics.models.EntityStatus
    :ivar source: This is a read-only legacy property. It is always set to
     'Azure' by the service. Kept here for backward compatibility.
    :vartype source: str
    :ivar customer_id: This is a read-only property. Represents the ID
     associated with the workspace.
    :vartype customer_id: str
    :ivar portal_url: This is a legacy property and is not used anymore. Kept
     here for backward compatibility.
    :vartype portal_url: str
    :param sku: The SKU of the workspace.
    :type sku: ~azure.mgmt.loganalytics.models.Sku
    :param retention_in_days: The workspace data retention in days. -1 means
     Unlimited retention for the Unlimited Sku. 730 days is the maximum allowed
     for all other Skus.
    :type retention_in_days: int
    :param e_tag: The ETag of the workspace.
    :type e_tag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'source': {'readonly': True},
        'customer_id': {'readonly': True},
        'portal_url': {'readonly': True},
        'retention_in_days': {'maximum': 730, 'minimum': -1},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'source': {'key': 'properties.source', 'type': 'str'},
        'customer_id': {'key': 'properties.customerId', 'type': 'str'},
        'portal_url': {'key': 'properties.portalUrl', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'Sku'},
        'retention_in_days': {'key': 'properties.retentionInDays', 'type': 'int'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Workspace, self).__init__(**kwargs)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.source = None
        self.customer_id = None
        self.portal_url = None
        self.sku = kwargs.get('sku', None)
        self.retention_in_days = kwargs.get('retention_in_days', None)
        self.e_tag = kwargs.get('e_tag', None)
