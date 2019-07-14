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


class IoTSecurityDeviceRecommendationsList(Model):
    """List of recommendations with the count of devices.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. List of aggregated recommendation data
    :type value:
     list[~azure.mgmt.security.models.IoTSecurityDeviceRecommendation]
    :ivar next_link: The URI to fetch the next page.
    :vartype next_link: str
    """

    _validation = {
        'value': {'required': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[IoTSecurityDeviceRecommendation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value, **kwargs) -> None:
        super(IoTSecurityDeviceRecommendationsList, self).__init__(**kwargs)
        self.value = value
        self.next_link = None
