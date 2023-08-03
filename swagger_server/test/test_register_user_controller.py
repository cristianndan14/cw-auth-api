# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_register_user_by_admin import RequestRegisterUserByAdmin  # noqa: E501
from swagger_server.models.response_register_user_by_admin import ResponseRegisterUserByAdmin  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRegisterUserController(BaseTestCase):
    """RegisterUserController integration test stubs"""

    def test_register_user(self):
        """Test case for register_user

        Registrar usuario
        """
        body = RequestRegisterUserByAdmin()
        response = self.client.open(
            '/registerUserByAdmin',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
