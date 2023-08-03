# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestAllUsers(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, external_transaction_id: str=None):  # noqa: E501
        """RequestAllUsers - a model defined in Swagger

        :param channel: The channel of this RequestAllUsers.  # noqa: E501
        :type channel: str
        :param external_transaction_id: The external_transaction_id of this RequestAllUsers.  # noqa: E501
        :type external_transaction_id: str
        """
        self.swagger_types = {
            'channel': str,
            'external_transaction_id': str
        }

        self.attribute_map = {
            'channel': 'channel',
            'external_transaction_id': 'externalTransactionId'
        }
        self._channel = channel
        self._external_transaction_id = external_transaction_id

    @classmethod
    def from_dict(cls, dikt) -> 'RequestAllUsers':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestAllUsers of this RequestAllUsers.  # noqa: E501
        :rtype: RequestAllUsers
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this RequestAllUsers.


        :return: The channel of this RequestAllUsers.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this RequestAllUsers.


        :param channel: The channel of this RequestAllUsers.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this RequestAllUsers.


        :return: The external_transaction_id of this RequestAllUsers.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this RequestAllUsers.


        :param external_transaction_id: The external_transaction_id of this RequestAllUsers.
        :type external_transaction_id: str
        """
        if external_transaction_id is None:
            raise ValueError("Invalid value for `external_transaction_id`, must not be `None`")  # noqa: E501

        self._external_transaction_id = external_transaction_id
