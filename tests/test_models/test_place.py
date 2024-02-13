#!/usr/bin/python3
"""Unittest for Place class"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class TestPlace(unittest.TestCase):
    """Unittest for Place class"""

    def test_default_attributes(self):
        """Test default attributes"""
        new_instance = Place()
        self.assertEqual(new_instance.city_id, "")
        self.assertEqual(new_instance.user_id, "")
        self.assertEqual(new_instance.name, "")
        self.assertEqual(new_instance.description, "")
        self.assertEqual(new_instance.number_rooms, 0)
        self.assertEqual(new_instance.number_bathrooms, 0)
        self.assertEqual(new_instance.max_guest, 0)
        self.assertEqual(new_instance.price_by_night, 0)
        self.assertEqual(new_instance.latitude, 0.0)
        self.assertEqual(new_instance.longitude, 0.0)
        self.assertEqual(new_instance.amenity_ids, [])

    def test_place_attributes(self):
        """Test place attributes"""
        new_instance = Place()
        new_instance.city_id = "NY"
        new_instance.user_id = "123e4567-e89b-12d3-a456-426614174000"
        new_instance.name = "New York"
        new_instance.description = "A city in the United States"
        new_instance.number_rooms = 5
        new_instance.number_bathrooms = 2
        new_instance.max_guest = 10
        new_instance.price_by_night = 100
        new_instance.latitude = 40.7128
        new_instance.longitude = -74.0060
        new_instance.amenity_ids = ["123e4567-e89b-12d3-a456-426614174000",
                                    "123e4567-e89b-12d3-a456-426614174001"]

        self.assertEqual(new_instance.city_id, "NY")
        self.assertEqual(new_instance.user_id,
                         "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(new_instance.name, "New York")
        self.assertEqual(new_instance.description,
                         "A city in the United States")
        self.assertEqual(new_instance.number_rooms, 5)
        self.assertEqual(new_instance.number_bathrooms, 2)
        self.assertEqual(new_instance.max_guest, 10)
        self.assertEqual(new_instance.price_by_night, 100)
        self.assertEqual(new_instance.latitude, 40.7128)
        self.assertEqual(new_instance.longitude, -74.0060)
        self.assertEqual(new_instance.amenity_ids, [
            "123e4567-e89b-12d3-a456-426614174000",
            "123e4567-e89b-12d3-a456-426614174001"
        ])

    def test_place_to_dict(self):
        """Test for to_dict method"""
        new_instance = Place()
        new_instance.name = "New York"
        new_instance.my_number = 89
        new_instance_dict = new_instance.to_dict()
        self.assertEqual(new_instance_dict['__class__'], 'Place')
        self.assertEqual(new_instance_dict['name'], 'New York')
        self.assertEqual(new_instance_dict['my_number'], 89)
        self.assertEqual(type(new_instance_dict['created_at']), str)
        self.assertEqual(type(new_instance_dict['updated_at']), str)

    def test_place_init_with_dict(self):
        """Test initialization with dictionary representation"""
        sample_dict = {
            'id': '123e4567-e89b-12d3-a456-426614174000',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'New York',
            'my_number': 89
        }

        new_instance = Place(**sample_dict)
        self.assertEqual(new_instance.id,
                         '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(type(new_instance.created_at), datetime)
        self.assertEqual(type(new_instance.updated_at), datetime)
        self.assertEqual(new_instance.name, 'New York')
        self.assertEqual(new_instance.my_number, 89)


if __name__ == '__main__':
    unittest.main()

