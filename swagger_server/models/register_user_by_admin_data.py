# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RegisterUserByAdminData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code_email: str=None, profile: str=None, name: str=None, phone: str=None, email: str=None, city: str=None, status: str=None, role_id: int=None):  # noqa: E501
        """RegisterUserByAdminData - a model defined in Swagger

        :param code_email: The code_email of this RegisterUserByAdminData.  # noqa: E501
        :type code_email: str
        :param profile: The profile of this RegisterUserByAdminData.  # noqa: E501
        :type profile: str
        :param name: The name of this RegisterUserByAdminData.  # noqa: E501
        :type name: str
        :param phone: The phone of this RegisterUserByAdminData.  # noqa: E501
        :type phone: str
        :param email: The email of this RegisterUserByAdminData.  # noqa: E501
        :type email: str
        :param city: The city of this RegisterUserByAdminData.  # noqa: E501
        :type city: str
        :param status: The status of this RegisterUserByAdminData.  # noqa: E501
        :type status: str
        :param role_id: The role_id of this RegisterUserByAdminData.  # noqa: E501
        :type role_id: int
        """
        self.swagger_types = {
            'code_email': str,
            'profile': str,
            'name': str,
            'phone': str,
            'email': str,
            'city': str,
            'status': str,
            'role_id': int
        }

        self.attribute_map = {
            'code_email': 'code_email',
            'profile': 'profile',
            'name': 'name',
            'phone': 'phone',
            'email': 'email',
            'city': 'city',
            'status': 'status',
            'role_id': 'role_id'
        }
        self._code_email = code_email
        self._profile = profile
        self._name = name
        self._phone = phone
        self._email = email
        self._city = city
        self._status = status
        self._role_id = role_id

    @classmethod
    def from_dict(cls, dikt) -> 'RegisterUserByAdminData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RegisterUserByAdminData of this RegisterUserByAdminData.  # noqa: E501
        :rtype: RegisterUserByAdminData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code_email(self) -> str:
        """Gets the code_email of this RegisterUserByAdminData.


        :return: The code_email of this RegisterUserByAdminData.
        :rtype: str
        """
        return self._code_email

    @code_email.setter
    def code_email(self, code_email: str):
        """Sets the code_email of this RegisterUserByAdminData.


        :param code_email: The code_email of this RegisterUserByAdminData.
        :type code_email: str
        """

        self._code_email = code_email

    @property
    def profile(self) -> str:
        """Gets the profile of this RegisterUserByAdminData.


        :return: The profile of this RegisterUserByAdminData.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile: str):
        """Sets the profile of this RegisterUserByAdminData.


        :param profile: The profile of this RegisterUserByAdminData.
        :type profile: str
        """

        self._profile = profile

    @property
    def name(self) -> str:
        """Gets the name of this RegisterUserByAdminData.


        :return: The name of this RegisterUserByAdminData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this RegisterUserByAdminData.


        :param name: The name of this RegisterUserByAdminData.
        :type name: str
        """

        self._name = name

    @property
    def phone(self) -> str:
        """Gets the phone of this RegisterUserByAdminData.


        :return: The phone of this RegisterUserByAdminData.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this RegisterUserByAdminData.


        :param phone: The phone of this RegisterUserByAdminData.
        :type phone: str
        """

        self._phone = phone

    @property
    def email(self) -> str:
        """Gets the email of this RegisterUserByAdminData.


        :return: The email of this RegisterUserByAdminData.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this RegisterUserByAdminData.


        :param email: The email of this RegisterUserByAdminData.
        :type email: str
        """

        self._email = email

    @property
    def city(self) -> str:
        """Gets the city of this RegisterUserByAdminData.


        :return: The city of this RegisterUserByAdminData.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this RegisterUserByAdminData.


        :param city: The city of this RegisterUserByAdminData.
        :type city: str
        """

        self._city = city

    @property
    def status(self) -> str:
        """Gets the status of this RegisterUserByAdminData.


        :return: The status of this RegisterUserByAdminData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this RegisterUserByAdminData.


        :param status: The status of this RegisterUserByAdminData.
        :type status: str
        """

        self._status = status

    @property
    def role_id(self) -> int:
        """Gets the role_id of this RegisterUserByAdminData.


        :return: The role_id of this RegisterUserByAdminData.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id: int):
        """Sets the role_id of this RegisterUserByAdminData.


        :param role_id: The role_id of this RegisterUserByAdminData.
        :type role_id: int
        """

        self._role_id = role_id
