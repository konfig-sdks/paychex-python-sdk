# coding: utf-8

"""
    External API

      # Developer Resources  Refer [Developer Resources](https://developer.paychex.com/resources/overview/) for more details on API specification 

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import paychex_python_sdk
from paychex_python_sdk.paths.checks import delete
from paychex_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestChecks(ApiTestMixin, unittest.TestCase):
    """
    Checks unit test stubs
        Checks by Pay Period and User
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
