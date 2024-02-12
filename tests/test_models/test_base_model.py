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
    """
    Test cases for the BaseModel class attributes and methods
    """

    def test_id_type(self):
        """Test for the type of id attribute"""
        my_model = BaseModel()
        self.assertEqual(type(my_model.id), str)

    def test_created_at_type(self):
        """Test for the type of created_at attribute"""
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)

    def test_updated_at_type(self):
        """Test for the type of updated_at attribute"""
        my_model = BaseModel()
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_str_representation(self):
        """Test for the __str__ representation"""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 89
        string = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(string, str(my_model))

    def test_save_method(self):
        """Test for the save method"""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 89
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test for the to_dict method"""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['name'], 'Test Model')
        self.assertEqual(my_model_dict['my_number'], 89)
        self.assertEqual(type(my_model_dict['created_at']), str)
        self.assertEqual(type(my_model_dict['updated_at']), str)

    def test_unique_id(self):
        """Test for unique id generation"""
        my_model = BaseModel()
        uuid1 = my_model.id
        my_model = BaseModel()
        uuid2 = my_model.id
        self.assertNotEqual(uuid1, uuid2)

    def test_init_with_dict_representation(self):
        """Test initialization with dictionary representation"""
        sample_dict = {
            'id': '123e4567-e89b-12d3-a456-426614174000',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:00:00.000000',
            'name': 'Test Model',
            'my_number': 42
        }

        new_model = BaseModel(**sample_dict)
        self.assertEqual(new_model.id, '123e4567-e89b-12d3-a456-426614174000')
        self.assertEqual(type(new_model.created_at), datetime)
        self.assertEqual(type(new_model.updated_at), datetime)
        self.assertEqual(new_model.name, 'Test Model')
        self.assertEqual(new_model.my_number, 42)

    def test_init_with_empty_dict(self):
        """Test initialization with an empty dictionary"""
        new_model = BaseModel(**{})
        self.assertNotEqual(new_model.id, None)
        self.assertEqual(type(new_model.created_at), datetime)
        self.assertEqual(type(new_model.updated_at), datetime)

    def test_save_method_file_storage(self):
        """Test if BaseModel instance is saved via FileStorage"""
        fs = FileStorage()
        new_model = BaseModel()
        fs.new(new_model)
        new_model.save()
        with open(fs._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn(new_model.id, data)

    def test_reload_method_file_storage(self):
        """Test if BaseModel instance is reloaded via FileStorage"""
        fs = FileStorage()
        new_model = BaseModel()
        fs.new(new_model)
        new_model.save()
        fs.reload()
        self.assertIn(
            f"{new_model.__class__.__name__}.{new_model.id}", fs.all())


if __name__ == '__main__':
    unittest.main()

