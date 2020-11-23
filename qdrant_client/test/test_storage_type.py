# coding: utf-8

"""
    Qdrant API

    API description for Qdrant vector search engine. Describes CRUD and search operations on collections of points (vectors with payload).  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: andrey@vasnetsov.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.storage_type_any_of import StorageTypeAnyOf
from openapi_client.model.storage_type_any_of1 import StorageTypeAnyOf1
globals()['StorageTypeAnyOf'] = StorageTypeAnyOf
globals()['StorageTypeAnyOf1'] = StorageTypeAnyOf1
from openapi_client.model.storage_type import StorageType


class TestStorageType(unittest.TestCase):
    """StorageType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStorageType(self):
        """Test StorageType"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StorageType()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
