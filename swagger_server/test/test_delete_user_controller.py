# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.response_delete_user import ResponseDeleteUser  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDeleteUserController(BaseTestCase):
    """DeleteUserController integration test stubs"""

    def test_delete_user(self):
        """Test case for delete_user

        Eliminar usuario.
        """
        response = self.client.open(
            '/users/{+code_email}'.format(code_email='code_email_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
