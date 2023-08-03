# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_reset_password import RequestResetPassword  # noqa: E501
from swagger_server.models.response_reset_password import ResponseResetPassword  # noqa: E501
from swagger_server.test import BaseTestCase


class TestResetPasswordController(BaseTestCase):
    """ResetPasswordController integration test stubs"""

    def test_reset_password(self):
        """Test case for reset_password

        Resetear password
        """
        body = RequestResetPassword()
        response = self.client.open(
            '/resetPassword',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
