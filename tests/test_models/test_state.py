#!/usr/bin/python3
"""Unittest for State"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """Unittest for State"""

    def test_default_attributes(self):
        """Test default attributes"""
        new_state_instance = State()
        self.assertEqual(new_state_instance.name, "")
        self.assertIsInstance(new_state_instance.created_at, datetime)
        self.assertIsInstance(new_state_instance.updated_at, datetime)
        self.assertIsInstance(new_state_instance.id, str)

    def test_state_init_with_dict(self):
        """Test initialization with dictionary representation"""
        sample_dict = {
            'id': '123e4567-e89b-12d3-a456-426614174000',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'New York'
        }

        new_state_instance = State(**sample_dict)

        self.assertEqual(new_state_instance.id,
                         '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(type(new_state_instance.created_at), datetime)
        self.assertEqual(type(new_state_instance.updated_at), datetime)
        self.assertEqual(new_state_instance.name, 'New York')

    def test_state_attributes(self):
        """Test state attributes"""
        new_state_instance = State()
        new_state_instance.name = "New York"
        self.assertEqual(new_state_instance.name, "New York")

    def test_state_to_dict(self):
        """Test for to_dict method"""
        new_state_instance = State()
        new_state_instance.name = "New York"
        new_state_instance.my_number = 89
        new_state_instance_dict = new_state_instance.to_dict()
        self.assertEqual(new_state_instance_dict['__class__'], 'State')
        self.assertEqual(new_state_instance_dict['name'], 'New York')
        self.assertEqual(new_state_instance_dict['my_number'], 89)
        self.assertEqual(type(new_state_instance_dict['created_at']), str)
        self.assertEqual(type(new_state_instance_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
