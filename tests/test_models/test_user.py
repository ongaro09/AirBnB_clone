#!/usr/bin/python3
"""Unittest for User class"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """Unittest for User class"""

    def test_default_attributes(self):
        """Test default attributes"""
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_user_attributes(self):
        """Test for user attributes"""
        new_user = User()
        new_user.email = "nessy@example.com"
        new_user.password = "mukami123"
        new_user.first_name = "Nessy"
        new_user.last_name = "Mukami"

        self.assertEqual(new_user.email, "nessy@example.com")
        self.assertEqual(new_user.password, "mukami123")
        self.assertEqual(new_user.first_name, "Nessy")
        self.assertEqual(new_user.last_name, "Mukami")

    def test_user_instance(self):
        """Test for user instance"""
        new_user = User()
        self.assertIsInstance(new_user, User)
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str(self):
        """Test User __str__ method"""
        user_data = {
            'id': '12345',
            'email': 'nessy@example.com',
            'password': 'mukami123',
            'first_name': 'Nessy',
            'last_name': 'Mukami'
        }
        new_user = User(**user_data)
        expected_str = "[User] ({}) {}".format(new_user.id, new_user.__dict__)
        self.assertEqual(str(new_user), expected_str)

    def test_user_save(self):
        """Test User save method"""
        new_user = User()
        old_updated_at = new_user.updated_at
        new_user.save()
        self.assertNotEqual(old_updated_at, new_user.updated_at)


if __name__ == '__main__':
    unittest.main()
