# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_check_user import RequestCheckUser  # noqa: E501
from swagger_server.models.response_check_user import ResponseCheckUser  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCheckUserController(BaseTestCase):
    """CheckUserController integration test stubs"""

    def test_get_user(self):
        """Test case for get_user

        Obtener un usuario
        """
        body = RequestCheckUser()
        response = self.client.open(
            '/checkUser',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
