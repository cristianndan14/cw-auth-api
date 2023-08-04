# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseTokenResetPasswordData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token_reset_password: str=None):  # noqa: E501
        """ResponseTokenResetPasswordData - a model defined in Swagger

        :param token_reset_password: The token_reset_password of this ResponseTokenResetPasswordData.  # noqa: E501
        :type token_reset_password: str
        """
        self.swagger_types = {
            'token_reset_password': str
        }

        self.attribute_map = {
            'token_reset_password': 'token_reset_password'
        }
        self._token_reset_password = token_reset_password

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseTokenResetPasswordData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseTokenResetPassword_data of this ResponseTokenResetPasswordData.  # noqa: E501
        :rtype: ResponseTokenResetPasswordData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token_reset_password(self) -> str:
        """Gets the token_reset_password of this ResponseTokenResetPasswordData.


        :return: The token_reset_password of this ResponseTokenResetPasswordData.
        :rtype: str
        """
        return self._token_reset_password

    @token_reset_password.setter
    def token_reset_password(self, token_reset_password: str):
        """Sets the token_reset_password of this ResponseTokenResetPasswordData.


        :param token_reset_password: The token_reset_password of this ResponseTokenResetPasswordData.
        :type token_reset_password: str
        """

        self._token_reset_password = token_reset_password