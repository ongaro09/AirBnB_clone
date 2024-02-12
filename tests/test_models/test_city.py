#!/usr/bin/python3
"""Unittest for City class."""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_default_attributes(self):
        """Test default attributes."""
        city_instance = City()
        self.assertEqual(city_instance.state_id, "")
        self.assertEqual(city_instance.name, "")
        self.assertIsInstance(city_instance.created_at, datetime)
        self.assertIsInstance(city_instance.updated_at, datetime)
        self.assertIsInstance(city_instance.id, str)

    def test_city_attributes(self):
        """Test city attributes."""
        city_instance = City()
        city_instance.state_id = "CA"
        city_instance.name = "Los Angeles"
        self.assertEqual(city_instance.state_id, "CA")
        self.assertEqual(city_instance.name, "Los Angeles")

    def test_city_init(self):
        """Test for City initialization."""
        city_instance = City()
        self.assertEqual(type(city_instance), City)

    def test_city_str(self):
        """Test for __str__ method."""
        city_instance = City()
        string_repr = "[City] ({}) {}".format(city_instance.id, city_instance.__dict__)
        self.assertEqual(string_repr, str(city_instance))

    def test_city_save(self):
        """Test for save method."""
        city_instance = City()
        city_instance.save()
        self.assertNotEqual(city_instance.created_at, city_instance.updated_at)

    def test_city_to_dict(self):
        """Test for to_dict method."""
        city_instance = City()
        city_instance.name = "San Francisco"
        city_instance.population = 884363
        city_dict = city_instance.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['name'], 'San Francisco')
        self.assertEqual(city_dict['population'], 884363)
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()

