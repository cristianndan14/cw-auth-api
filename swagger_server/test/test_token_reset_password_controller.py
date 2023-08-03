# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_token_reset_password import RequestTokenResetPassword  # noqa: E501
from swagger_server.models.response_token_reset_password import ResponseTokenResetPassword  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTokenResetPasswordController(BaseTestCase):
    """TokenResetPasswordController integration test stubs"""

    def test_token_reset_password(self):
        """Test case for token_reset_password

        Generar token para resetear password
        """
        body = RequestTokenResetPassword()
        response = self.client.open(
            '/tokenResetPassword',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
