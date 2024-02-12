#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import uuid


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def test_unique_id_type(self):
        """Test for the type of the custom_id attribute"""
        my_instance = BaseModel()
        self.assertEqual(type(my_instance.custom_id), str)

    def test_created_at_type(self):
        """Test for the type of the created_timestamp attribute"""
        my_instance = BaseModel()
        self.assertEqual(type(my_instance.created_timestamp), datetime)

    def test_updated_at_type(self):
        """Test for the type of the updated_timestamp attribute"""
        my_instance = BaseModel()
        self.assertEqual(type(my_instance.updated_timestamp), datetime)

    def test_str_representation(self):
        """Test for the __str__ method"""
        my_instance = BaseModel()
        my_instance.name = "My Instance"
        my_instance.my_number = 89
        string = "[BaseModel] ({}) {}".format(my_instance.custom_id, my_instance.__dict__)
        self.assertEqual(string, str(my_instance))

    def test_save_method(self):
        """Test for the save method"""
        my_instance = BaseModel()
        my_instance.name = "My Instance"
        my_instance.my_number = 89
        my_instance.save()
        self.assertNotEqual(my_instance.created_timestamp, my_instance.updated_timestamp)

    def test_to_dict_method(self):
        """Test for the to_dict method"""
        my_instance = BaseModel()
        my_instance.name = "My Instance"
        my_instance.my_number = 89
        my_instance_dict = my_instance.to_dict()
        self.assertEqual(my_instance_dict['__class__'], 'BaseModel')
        self.assertEqual(my_instance_dict['name'], 'My Instance')
        self.assertEqual(my_instance_dict['my_number'], 89)
        self.assertEqual(type(my_instance_dict['created_at']), str)
        self.assertEqual(type(my_instance_dict['updated_at']), str)

    def test_unique_id(self):
        """Test for the generation of unique ids"""
        my_instance = BaseModel()
        uuid1 = my_instance.custom_id
        my_instance = BaseModel()
        uuid2 = my_instance.custom_id
        self.assertNotEqual(uuid1, uuid2)

    def test_init_with_dict_representation(self):
        """Test initialization with dictionary representation"""
        sample_dict = {
            'custom_id': '123e4567-e89b-12d3-a456-426614174000',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'Test Instance',
            'my_number': 42
        }

        new_instance = BaseModel(**sample_dict)
        self.assertEqual(new_instance.custom_id, '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(type(new_instance.created_at), datetime)
        self.assertEqual(type(new_instance.updated_at), datetime)
        self.assertEqual(new_instance.name, 'Test Instance')
        self.assertEqual(new_instance.my_number, 42)

    def test_init_with_empty_dict(self):
        """Test initialization with an empty dictionary"""
        new_instance = BaseModel(**{})
        self.assertNotEqual(new_instance.custom_id, None)
        self.assertEqual(type(new_instance.created_at), datetime)
        self.assertEqual(type(new_instance.updated_at), datetime)

    def test_init_with_single_attribute_dict(self):
        """
        Test initialization with a dictionary containing a single attribute
        """
        sample_dict = {'name': 'Single Attribute'}
        new_instance = BaseModel(**sample_dict)
        self.assertEqual(new_instance.name, 'Single Attribute')

    def test_init_with_invalid_attribute(self):
        """Test initialization with an invalid attribute"""
        sample_dict = {'name': 'Invalid Attribute', 'invalid': 'Invalid'}
        new_instance = BaseModel(**sample_dict)
        self.assertEqual(new_instance.name, 'Invalid Attribute')

    def test_save_method_file_storage(self):
        """Test if BaseModel instance is saved via FileStorage"""
        fs = FileStorage()
        new_instance = BaseModel()
        fs.new(new_instance)
        new_instance.save()
        with open(fs._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn(new_instance.custom_id, data)

    def test_reload_method_file_storage(self):
        """Test if BaseModel instance is reloaded via FileStorage"""
        fs = FileStorage()
        new_instance = BaseModel()
        fs.new(new_instance)
        new_instance.save()
        fs.reload()
        self.assertIn(
                f"{new_instance.__class__.__name__}.{new_instance.custom_id}", fs.all())


if __name__ == '__main__':
    unittest.main()

