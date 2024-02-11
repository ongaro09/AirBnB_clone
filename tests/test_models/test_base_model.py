#!/usr/bin/python3
"""
Test suite for the BaseModel class
"""

import os
import re
import json
import uuid
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class attributes and methods
    """

    def setUp(self):
        """
        Preparation for testing
        """
        pass

    def test_basic_attributes(self):
        """
        Test basic attributes assignment and retrieval
        """
        my_model = BaseModel()
        my_model.name = "AirBnB Clone"
        my_model.value = 42
        self.assertEqual([my_model.name, my_model.value],
                         ["AirBnB Clone", 42])

    def test_datetime_format(self):
        """
        Test the format of datetime attributes
        """
        pass
    
    def test_updated_at(self):
        """
        Test the updated_at attribute after calling save()
        """
        pass


if __name__ == '__main__':
    unittest.main()
