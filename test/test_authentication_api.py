# coding: utf-8

"""
    Kubernetes Queen API

    A simple API to interact with Kubernetes clusters

    OpenAPI spec version: 0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.TestCase):
    """ AuthenticationApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.authentication_api.AuthenticationApi()

    def tearDown(self):
        pass

    def test_auth_post(self):
        """
        Test case for auth_post

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
