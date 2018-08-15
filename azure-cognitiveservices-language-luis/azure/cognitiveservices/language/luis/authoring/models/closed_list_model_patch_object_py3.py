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


class ClosedListModelPatchObject(Model):
    """Object model for adding a batch of sublists to an existing closedlist.

    :param sub_lists: Sublists to add.
    :type sub_lists:
     list[~azure.cognitiveservices.language.luis.authoring.models.WordListObject]
    """

    _attribute_map = {
        'sub_lists': {'key': 'subLists', 'type': '[WordListObject]'},
    }

    def __init__(self, *, sub_lists=None, **kwargs) -> None:
        super(ClosedListModelPatchObject, self).__init__(**kwargs)
        self.sub_lists = sub_lists
