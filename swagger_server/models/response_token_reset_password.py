# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseTokenResetPassword(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: str=None, message: str=None, internal_transaction_id: str=None, external_transaction_id: str=None, data: object=None):  # noqa: E501
        """ResponseTokenResetPassword - a model defined in Swagger

        :param code: The code of this ResponseTokenResetPassword.  # noqa: E501
        :type code: str
        :param message: The message of this ResponseTokenResetPassword.  # noqa: E501
        :type message: str
        :param internal_transaction_id: The internal_transaction_id of this ResponseTokenResetPassword.  # noqa: E501
        :type internal_transaction_id: str
        :param external_transaction_id: The external_transaction_id of this ResponseTokenResetPassword.  # noqa: E501
        :type external_transaction_id: str
        :param data: The data of this ResponseTokenResetPassword.  # noqa: E501
        :type data: object
        """
        self.swagger_types = {
            'code': str,
            'message': str,
            'internal_transaction_id': str,
            'external_transaction_id': str,
            'data': object
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'internal_transaction_id': 'internalTransactionId',
            'external_transaction_id': 'externalTransactionId',
            'data': 'data'
        }
        self._code = code
        self._message = message
        self._internal_transaction_id = internal_transaction_id
        self._external_transaction_id = external_transaction_id
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseTokenResetPassword':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseTokenResetPassword of this ResponseTokenResetPassword.  # noqa: E501
        :rtype: ResponseTokenResetPassword
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this ResponseTokenResetPassword.


        :return: The code of this ResponseTokenResetPassword.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this ResponseTokenResetPassword.


        :param code: The code of this ResponseTokenResetPassword.
        :type code: str
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this ResponseTokenResetPassword.


        :return: The message of this ResponseTokenResetPassword.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseTokenResetPassword.


        :param message: The message of this ResponseTokenResetPassword.
        :type message: str
        """

        self._message = message

    @property
    def internal_transaction_id(self) -> str:
        """Gets the internal_transaction_id of this ResponseTokenResetPassword.


        :return: The internal_transaction_id of this ResponseTokenResetPassword.
        :rtype: str
        """
        return self._internal_transaction_id

    @internal_transaction_id.setter
    def internal_transaction_id(self, internal_transaction_id: str):
        """Sets the internal_transaction_id of this ResponseTokenResetPassword.


        :param internal_transaction_id: The internal_transaction_id of this ResponseTokenResetPassword.
        :type internal_transaction_id: str
        """

        self._internal_transaction_id = internal_transaction_id

    @property
    def external_transaction_id(self) -> str:
        """Gets the external_transaction_id of this ResponseTokenResetPassword.


        :return: The external_transaction_id of this ResponseTokenResetPassword.
        :rtype: str
        """
        return self._external_transaction_id

    @external_transaction_id.setter
    def external_transaction_id(self, external_transaction_id: str):
        """Sets the external_transaction_id of this ResponseTokenResetPassword.


        :param external_transaction_id: The external_transaction_id of this ResponseTokenResetPassword.
        :type external_transaction_id: str
        """

        self._external_transaction_id = external_transaction_id

    @property
    def data(self) -> object:
        """Gets the data of this ResponseTokenResetPassword.


        :return: The data of this ResponseTokenResetPassword.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data: object):
        """Sets the data of this ResponseTokenResetPassword.


        :param data: The data of this ResponseTokenResetPassword.
        :type data: object
        """

        self._data = data
