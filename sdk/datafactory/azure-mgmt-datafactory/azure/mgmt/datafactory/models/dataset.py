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


class Dataset(Model):
    """The Azure Data Factory nested object which identifies data within different
    data stores, such as tables, files, folders, and documents.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: GoogleAdWordsObjectDataset, AzureDataExplorerTableDataset,
    OracleServiceCloudObjectDataset, DynamicsAXResourceDataset,
    ResponsysObjectDataset, SalesforceMarketingCloudObjectDataset,
    VerticaTableDataset, NetezzaTableDataset, ZohoObjectDataset,
    XeroObjectDataset, SquareObjectDataset, SparkObjectDataset,
    ShopifyObjectDataset, ServiceNowObjectDataset, QuickBooksObjectDataset,
    PrestoObjectDataset, PhoenixObjectDataset, PaypalObjectDataset,
    MarketoObjectDataset, AzureMariaDBTableDataset, MariaDBTableDataset,
    MagentoObjectDataset, JiraObjectDataset, ImpalaObjectDataset,
    HubspotObjectDataset, HiveObjectDataset, HBaseObjectDataset,
    GreenplumTableDataset, GoogleBigQueryObjectDataset, EloquaObjectDataset,
    DrillTableDataset, CouchbaseTableDataset, ConcurObjectDataset,
    AzurePostgreSqlTableDataset, AmazonMWSObjectDataset, HttpDataset,
    AzureSearchIndexDataset, WebTableDataset, SapTableResourceDataset,
    RestResourceDataset, SqlServerTableDataset, SapOpenHubTableDataset,
    SapHanaTableDataset, SapEccResourceDataset,
    SapCloudForCustomerResourceDataset, SapBwCubeDataset, SybaseTableDataset,
    SalesforceServiceCloudObjectDataset, SalesforceObjectDataset,
    MicrosoftAccessTableDataset, PostgreSqlTableDataset, MySqlTableDataset,
    OdbcTableDataset, InformixTableDataset, RelationalTableDataset,
    AzureMySqlTableDataset, TeradataTableDataset, OracleTableDataset,
    ODataResourceDataset, CosmosDbMongoDbApiCollectionDataset,
    MongoDbV2CollectionDataset, MongoDbCollectionDataset, FileShareDataset,
    Office365Dataset, AzureBlobFSDataset, AzureDataLakeStoreDataset,
    CommonDataServiceForAppsEntityDataset, DynamicsCrmEntityDataset,
    DynamicsEntityDataset, DocumentDbCollectionDataset, CustomDataset,
    CassandraTableDataset, AzureSqlDWTableDataset, AzureSqlMITableDataset,
    AzureSqlTableDataset, AzureTableDataset, AzureBlobDataset, BinaryDataset,
    DelimitedTextDataset, ParquetDataset, AvroDataset, AmazonS3Dataset

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Dataset description.
    :type description: str
    :param structure: Columns that define the structure of the dataset. Type:
     array (or Expression with resultType array), itemType: DatasetDataElement.
    :type structure: object
    :param schema: Columns that define the physical type schema of the
     dataset. Type: array (or Expression with resultType array), itemType:
     DatasetSchemaDataElement.
    :type schema: object
    :param linked_service_name: Required. Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param parameters: Parameters for dataset.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param folder: The folder that this Dataset is in. If not specified,
     Dataset will appear at the root level.
    :type folder: ~azure.mgmt.datafactory.models.DatasetFolder
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'linked_service_name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'structure': {'key': 'structure', 'type': 'object'},
        'schema': {'key': 'schema', 'type': 'object'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'folder': {'key': 'folder', 'type': 'DatasetFolder'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'GoogleAdWordsObject': 'GoogleAdWordsObjectDataset', 'AzureDataExplorerTable': 'AzureDataExplorerTableDataset', 'OracleServiceCloudObject': 'OracleServiceCloudObjectDataset', 'DynamicsAXResource': 'DynamicsAXResourceDataset', 'ResponsysObject': 'ResponsysObjectDataset', 'SalesforceMarketingCloudObject': 'SalesforceMarketingCloudObjectDataset', 'VerticaTable': 'VerticaTableDataset', 'NetezzaTable': 'NetezzaTableDataset', 'ZohoObject': 'ZohoObjectDataset', 'XeroObject': 'XeroObjectDataset', 'SquareObject': 'SquareObjectDataset', 'SparkObject': 'SparkObjectDataset', 'ShopifyObject': 'ShopifyObjectDataset', 'ServiceNowObject': 'ServiceNowObjectDataset', 'QuickBooksObject': 'QuickBooksObjectDataset', 'PrestoObject': 'PrestoObjectDataset', 'PhoenixObject': 'PhoenixObjectDataset', 'PaypalObject': 'PaypalObjectDataset', 'MarketoObject': 'MarketoObjectDataset', 'AzureMariaDBTable': 'AzureMariaDBTableDataset', 'MariaDBTable': 'MariaDBTableDataset', 'MagentoObject': 'MagentoObjectDataset', 'JiraObject': 'JiraObjectDataset', 'ImpalaObject': 'ImpalaObjectDataset', 'HubspotObject': 'HubspotObjectDataset', 'HiveObject': 'HiveObjectDataset', 'HBaseObject': 'HBaseObjectDataset', 'GreenplumTable': 'GreenplumTableDataset', 'GoogleBigQueryObject': 'GoogleBigQueryObjectDataset', 'EloquaObject': 'EloquaObjectDataset', 'DrillTable': 'DrillTableDataset', 'CouchbaseTable': 'CouchbaseTableDataset', 'ConcurObject': 'ConcurObjectDataset', 'AzurePostgreSqlTable': 'AzurePostgreSqlTableDataset', 'AmazonMWSObject': 'AmazonMWSObjectDataset', 'HttpFile': 'HttpDataset', 'AzureSearchIndex': 'AzureSearchIndexDataset', 'WebTable': 'WebTableDataset', 'SapTableResource': 'SapTableResourceDataset', 'RestResource': 'RestResourceDataset', 'SqlServerTable': 'SqlServerTableDataset', 'SapOpenHubTable': 'SapOpenHubTableDataset', 'SapHanaTable': 'SapHanaTableDataset', 'SapEccResource': 'SapEccResourceDataset', 'SapCloudForCustomerResource': 'SapCloudForCustomerResourceDataset', 'SapBwCube': 'SapBwCubeDataset', 'SybaseTable': 'SybaseTableDataset', 'SalesforceServiceCloudObject': 'SalesforceServiceCloudObjectDataset', 'SalesforceObject': 'SalesforceObjectDataset', 'MicrosoftAccessTable': 'MicrosoftAccessTableDataset', 'PostgreSqlTable': 'PostgreSqlTableDataset', 'MySqlTable': 'MySqlTableDataset', 'OdbcTable': 'OdbcTableDataset', 'InformixTable': 'InformixTableDataset', 'RelationalTable': 'RelationalTableDataset', 'Db2Table': 'Db2TableDataset', 'AmazonRedshiftTable': 'AmazonRedshiftTableDataset', 'AzureMySqlTable': 'AzureMySqlTableDataset', 'TeradataTable': 'TeradataTableDataset', 'OracleTable': 'OracleTableDataset', 'ODataResource': 'ODataResourceDataset', 'CosmosDbMongoDbApiCollection': 'CosmosDbMongoDbApiCollectionDataset', 'MongoDbV2Collection': 'MongoDbV2CollectionDataset', 'MongoDbCollection': 'MongoDbCollectionDataset', 'FileShare': 'FileShareDataset', 'Office365Table': 'Office365Dataset', 'AzureBlobFSFile': 'AzureBlobFSDataset', 'AzureDataLakeStoreFile': 'AzureDataLakeStoreDataset', 'CommonDataServiceForAppsEntity': 'CommonDataServiceForAppsEntityDataset', 'DynamicsCrmEntity': 'DynamicsCrmEntityDataset', 'DynamicsEntity': 'DynamicsEntityDataset', 'DocumentDbCollection': 'DocumentDbCollectionDataset', 'CustomDataset': 'CustomDataset', 'CassandraTable': 'CassandraTableDataset', 'AzureSqlDWTable': 'AzureSqlDWTableDataset', 'AzureSqlMITable': 'AzureSqlMITableDataset', 'AzureSqlTable': 'AzureSqlTableDataset', 'AzureTable': 'AzureTableDataset', 'AzureBlob': 'AzureBlobDataset', 'Binary': 'BinaryDataset', 'DelimitedText': 'DelimitedTextDataset', 'Parquet': 'ParquetDataset', 'Avro': 'AvroDataset', 'AmazonS3Object': 'AmazonS3Dataset'}
    }

    def __init__(self, **kwargs):
        super(Dataset, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.description = kwargs.get('description', None)
        self.structure = kwargs.get('structure', None)
        self.schema = kwargs.get('schema', None)
        self.linked_service_name = kwargs.get('linked_service_name', None)
        self.parameters = kwargs.get('parameters', None)
        self.annotations = kwargs.get('annotations', None)
        self.folder = kwargs.get('folder', None)
        self.type = None
