# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.signin_signup_user_data import SigninSignupUserData  # noqa: F401,E501
from swagger_server import util


class RequestSignin(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, external_transaction_id: str=None, data: SigninSignupUserData=None):  # noqa: E501
        """RequestSignin - a model defined in Swagger

        :param channel: The channel of this RequestSignin.  # noqa: E501
        :type channel: str
        :param external_transaction_id: The external_transaction_id of this RequestSignin.  # noqa: E501
        :type external_transaction_id: str
        :param data: The data of this RequestSignin.  # noqa: E501
        :type data: SigninSignupUserData
        """
        self.swagger_types = {
            'channel': str,
            'external_transaction_id': str,
            'data': SigninSignupUserData
        }

        self.attribute_map = {
            'channel': 'channel',
            'external_transaction_id': 'externalTransactionId',
            'data': 'data'
        }
        self._channel = channel
        self._external_transaction_id = external_transaction_id
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'RequestSignin':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestSignin of this RequestSignin.  # noqa: E501
        :rtype: RequestSignin
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this RequestSignin.


        :return: The channel of this RequestSignin.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this RequestSignin.


        :param channel: The channel of this RequestSignin.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this RequestSignin.


        :return: The external_transaction_id of this RequestSignin.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this RequestSignin.


        :param external_transaction_id: The external_transaction_id of this RequestSignin.
        :type external_transaction_id: str
        """
        if external_transaction_id is None:
            raise ValueError("Invalid value for `external_transaction_id`, must not be `None`")  # noqa: E501

        self._external_transaction_id = external_transaction_id

    @property
    def data(self) -> SigninSignupUserData:
        """Gets the data of this RequestSignin.


        :return: The data of this RequestSignin.
        :rtype: SigninSignupUserData
        """
        return self._data

    @data.setter
    def data(self, data: SigninSignupUserData):
        """Sets the data of this RequestSignin.


        :param data: The data of this RequestSignin.
        :type data: SigninSignupUserData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
