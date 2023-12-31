# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code_email: str=None, status: bool=None, role_id: int=None, user_type: str=None, name: str=None, last_name: str=None, city: str=None, address: str=None, email: str=None, cellphone: str=None, department: str=None, identification_number: str=None, entry_date: str=None, password: str=None):  # noqa: E501
        """UserData - a model defined in Swagger

        :param code_email: The code_email of this UserData.  # noqa: E501
        :type code_email: str
        :param status: The status of this UserData.  # noqa: E501
        :type status: bool
        :param role_id: The role_id of this UserData.  # noqa: E501
        :type role_id: int
        :param user_type: The user_type of this UserData.  # noqa: E501
        :type user_type: str
        :param name: The name of this UserData.  # noqa: E501
        :type name: str
        :param last_name: The last_name of this UserData.  # noqa: E501
        :type last_name: str
        :param city: The city of this UserData.  # noqa: E501
        :type city: str
        :param address: The address of this UserData.  # noqa: E501
        :type address: str
        :param email: The email of this UserData.  # noqa: E501
        :type email: str
        :param cellphone: The cellphone of this UserData.  # noqa: E501
        :type cellphone: str
        :param department: The department of this UserData.  # noqa: E501
        :type department: str
        :param identification_number: The identification_number of this UserData.  # noqa: E501
        :type identification_number: str
        :param entry_date: The entry_date of this UserData.  # noqa: E501
        :type entry_date: str
        :param password: The password of this UserData.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'code_email': str,
            'status': bool,
            'role_id': int,
            'user_type': str,
            'name': str,
            'last_name': str,
            'city': str,
            'address': str,
            'email': str,
            'cellphone': str,
            'department': str,
            'identification_number': str,
            'entry_date': str,
            'password': str
        }

        self.attribute_map = {
            'code_email': 'code_email',
            'status': 'status',
            'role_id': 'role_id',
            'user_type': 'user_type',
            'name': 'name',
            'last_name': 'last_name',
            'city': 'city',
            'address': 'address',
            'email': 'email',
            'cellphone': 'cellphone',
            'department': 'department',
            'identification_number': 'identification_number',
            'entry_date': 'entry_date',
            'password': 'password'
        }
        self._code_email = code_email
        self._status = status
        self._role_id = role_id
        self._user_type = user_type
        self._name = name
        self._last_name = last_name
        self._city = city
        self._address = address
        self._email = email
        self._cellphone = cellphone
        self._department = department
        self._identification_number = identification_number
        self._entry_date = entry_date
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'UserData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserData of this UserData.  # noqa: E501
        :rtype: UserData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code_email(self) -> str:
        """Gets the code_email of this UserData.


        :return: The code_email of this UserData.
        :rtype: str
        """
        return self._code_email

    @code_email.setter
    def code_email(self, code_email: str):
        """Sets the code_email of this UserData.


        :param code_email: The code_email of this UserData.
        :type code_email: str
        """

        self._code_email = code_email

    @property
    def status(self) -> bool:
        """Gets the status of this UserData.


        :return: The status of this UserData.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status: bool):
        """Sets the status of this UserData.


        :param status: The status of this UserData.
        :type status: bool
        """

        self._status = status

    @property
    def role_id(self) -> int:
        """Gets the role_id of this UserData.


        :return: The role_id of this UserData.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id: int):
        """Sets the role_id of this UserData.


        :param role_id: The role_id of this UserData.
        :type role_id: int
        """

        self._role_id = role_id

    @property
    def user_type(self) -> str:
        """Gets the user_type of this UserData.


        :return: The user_type of this UserData.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type: str):
        """Sets the user_type of this UserData.


        :param user_type: The user_type of this UserData.
        :type user_type: str
        """

        self._user_type = user_type

    @property
    def name(self) -> str:
        """Gets the name of this UserData.


        :return: The name of this UserData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this UserData.


        :param name: The name of this UserData.
        :type name: str
        """

        self._name = name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this UserData.


        :return: The last_name of this UserData.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this UserData.


        :param last_name: The last_name of this UserData.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def city(self) -> str:
        """Gets the city of this UserData.


        :return: The city of this UserData.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this UserData.


        :param city: The city of this UserData.
        :type city: str
        """

        self._city = city

    @property
    def address(self) -> str:
        """Gets the address of this UserData.


        :return: The address of this UserData.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this UserData.


        :param address: The address of this UserData.
        :type address: str
        """

        self._address = address

    @property
    def email(self) -> str:
        """Gets the email of this UserData.


        :return: The email of this UserData.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserData.


        :param email: The email of this UserData.
        :type email: str
        """

        self._email = email

    @property
    def cellphone(self) -> str:
        """Gets the cellphone of this UserData.


        :return: The cellphone of this UserData.
        :rtype: str
        """
        return self._cellphone

    @cellphone.setter
    def cellphone(self, cellphone: str):
        """Sets the cellphone of this UserData.


        :param cellphone: The cellphone of this UserData.
        :type cellphone: str
        """

        self._cellphone = cellphone

    @property
    def department(self) -> str:
        """Gets the department of this UserData.


        :return: The department of this UserData.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department: str):
        """Sets the department of this UserData.


        :param department: The department of this UserData.
        :type department: str
        """

        self._department = department

    @property
    def identification_number(self) -> str:
        """Gets the identification_number of this UserData.


        :return: The identification_number of this UserData.
        :rtype: str
        """
        return self._identification_number

    @identification_number.setter
    def identification_number(self, identification_number: str):
        """Sets the identification_number of this UserData.


        :param identification_number: The identification_number of this UserData.
        :type identification_number: str
        """

        self._identification_number = identification_number

    @property
    def entry_date(self) -> str:
        """Gets the entry_date of this UserData.


        :return: The entry_date of this UserData.
        :rtype: str
        """
        return self._entry_date

    @entry_date.setter
    def entry_date(self, entry_date: str):
        """Sets the entry_date of this UserData.


        :param entry_date: The entry_date of this UserData.
        :type entry_date: str
        """

        self._entry_date = entry_date

    @property
    def password(self) -> str:
        """Gets the password of this UserData.


        :return: The password of this UserData.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this UserData.


        :param password: The password of this UserData.
        :type password: str
        """

        self._password = password
