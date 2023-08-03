# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_signin import RequestSignin  # noqa: E501
from swagger_server.models.response_signin import ResponseSignin  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSigninUsersController(BaseTestCase):
    """SigninUsersController integration test stubs"""

    def test_signin(self):
        """Test case for signin

        Inicio de sesion de usuarios
        """
        body = RequestSignin()
        response = self.client.open(
            '/signin',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
