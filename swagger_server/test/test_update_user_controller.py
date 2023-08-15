# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_update_user import RequestUpdateUser  # noqa: E501
from swagger_server.models.response_update_user import ResponseUpdateUser  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUpdateUserController(BaseTestCase):
    """UpdateUserController integration test stubs"""

    def test_update_user(self):
        """Test case for update_user

        Actualizar usuario.
        """
        body = RequestUpdateUser()
        response = self.client.open(
            '/users/{code_email}'.format(code_email='code_email_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
