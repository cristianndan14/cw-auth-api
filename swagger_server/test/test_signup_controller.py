# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_signup import RequestSignup  # noqa: E501
from swagger_server.models.response_signup import ResponseSignup  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSignupController(BaseTestCase):
    """SignupController integration test stubs"""

    def test_signup(self):
        """Test case for signup

        Registrar vendedor
        """
        body = RequestSignup()
        response = self.client.open(
            '/signup',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
