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


class RecommendationConfigurationProperties(Model):
    """Recommendation configuration.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param recommendation_type: Required. The recommendation type. Possible
     values include: 'OpenPortsOnDevice', 'PermissiveFirewallPolicy',
     'PermissiveFirewallRuleInput', 'PermissiveFirewallRuleOut',
     'OperationSystemNotValid', 'UnutilizedMessagesFromAgent',
     'SecurityTwinConfigurationNotOptimal',
     'SecurityTwinConfigurationConflict', 'IdenticalAuthenticationCredentials',
     'DenyDefaultIpPolicy', 'TooLargeIPRange', 'EnableDiagnosticsLog'
    :type recommendation_type: str or
     ~azure.mgmt.security.models.RecommendationType
    :ivar description:
    :vartype description: str
    :param status: Required. Recommendation status. The recommendation is not
     generated when the status is turned off. Possible values include:
     'TurnedOff', 'TurnedOn'. Default value: "TurnedOn" .
    :type status: str or
     ~azure.mgmt.security.models.RecommendationConfigStatus
    """

    _validation = {
        'recommendation_type': {'required': True},
        'description': {'readonly': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'recommendation_type': {'key': 'recommendationType', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, *, recommendation_type, status="TurnedOn", **kwargs) -> None:
        super(RecommendationConfigurationProperties, self).__init__(**kwargs)
        self.recommendation_type = recommendation_type
        self.description = None
        self.status = status
