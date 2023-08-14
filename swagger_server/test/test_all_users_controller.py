# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_all_users import RequestAllUsers  # noqa: E501
from swagger_server.models.response_all_users import ResponseAllUsers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAllUsersController(BaseTestCase):
    """AllUsersController integration test stubs"""

    def test_all_users(self):
        """Test case for all_users

        Obtener todos los usuarios
        """
        body = RequestAllUsers()
        response = self.client.open(
            '/allUsers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
