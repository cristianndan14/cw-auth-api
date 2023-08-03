# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestCheckUser(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, external_transaction_id: str=None, code_email: str=None):  # noqa: E501
        """RequestCheckUser - a model defined in Swagger

        :param channel: The channel of this RequestCheckUser.  # noqa: E501
        :type channel: str
        :param external_transaction_id: The external_transaction_id of this RequestCheckUser.  # noqa: E501
        :type external_transaction_id: str
        :param code_email: The code_email of this RequestCheckUser.  # noqa: E501
        :type code_email: str
        """
        self.swagger_types = {
            'channel': str,
            'external_transaction_id': str,
            'code_email': str
        }

        self.attribute_map = {
            'channel': 'channel',
            'external_transaction_id': 'externalTransactionId',
            'code_email': 'code_email'
        }
        self._channel = channel
        self._external_transaction_id = external_transaction_id
        self._code_email = code_email

    @classmethod
    def from_dict(cls, dikt) -> 'RequestCheckUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestCheckUser of this RequestCheckUser.  # noqa: E501
        :rtype: RequestCheckUser
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this RequestCheckUser.


        :return: The channel of this RequestCheckUser.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this RequestCheckUser.


        :param channel: The channel of this RequestCheckUser.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this RequestCheckUser.


        :return: The external_transaction_id of this RequestCheckUser.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this RequestCheckUser.


        :param external_transaction_id: The external_transaction_id of this RequestCheckUser.
        :type external_transaction_id: str
        """
        if external_transaction_id is None:
            raise ValueError("Invalid value for `external_transaction_id`, must not be `None`")  # noqa: E501

        self._external_transaction_id = external_transaction_id

    @property
    def code_email(self) -> str:
        """Gets the code_email of this RequestCheckUser.


        :return: The code_email of this RequestCheckUser.
        :rtype: str
        """
        return self._code_email

    @code_email.setter
    def code_email(self, code_email: str):
        """Sets the code_email of this RequestCheckUser.


        :param code_email: The code_email of this RequestCheckUser.
        :type code_email: str
        """
        if code_email is None:
            raise ValueError("Invalid value for `code_email`, must not be `None`")  # noqa: E501

        self._code_email = code_email
