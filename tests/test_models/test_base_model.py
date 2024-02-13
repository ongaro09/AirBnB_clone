#!/usr/bin/python3
"""The module includes unittest classes for testing various functionalities
    of the BaseModel class:
    - TestBaseModelInstantiation: Tests instantiation of the BaseModel class.
    - TestBaseModelSave: Tests the save method of the BaseModel class.
    - TestBaseModelToDict: Tests the to_dict method of the BaseModel class.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_two_models_different_created_at(self):
        base_model_1 = BaseModel()
        sleep(0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.created_at, base_model_2.created_at)

    def test_two_models_different_updated_at(self):
        base_model_1 = BaseModel()
        sleep(0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.updated_at, base_model_2.updated_at)


    def test_string_representation(self):
        current_datetime = datetime.today()
        datetime_repr = repr(current_datetime)
        base_model = BaseModel()
        base_model.id = "123456"
        base_model.created_at = base_model.updated_at = current_datetime
        base_model_str = base_model.__str__()
        self.assertIn("[BaseModel] (123456)", base_model_str)
        self.assertIn("'id': '123456'", base_model_str)
        self.assertIn("'created_at': " + datetime_repr, base_model_str)
        self.assertIn("'updated_at': " + datetime_repr, base_model_str)


    def test_unused_args(self):
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        current_datetime = datetime.today()
        current_datetime_iso = current_datetime.isoformat()
        base_model = BaseModel(id="345", created_at=current_datetime_iso, updated_at=current_datetime_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, current_datetime)
        self.assertEqual(base_model.updated_at, current_datetime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        current_datetime = datetime.today()
        current_datetime_iso = current_datetime.isoformat()
        base_model = BaseModel("12", id="345", created_at=current_datetime_iso, updated_at=current_datetime_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, current_datetime)
        self.assertEqual(base_model.updated_at, current_datetime)


class TestBaseModel_save(unittest.TestCase):
    """Unit tests for the save method of the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Set up class method to prepare for test execution."""
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to clean up after test execution."""
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename('tmp', 'file.json')
        except IOError:
            pass

    def test_one_save(self):
        """Test whether saving a BaseModel instance
        updates its 'updated_at' attribute.
        """
        base_model = BaseModel()
        sleep(0.05)
        first_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(first_updated_at, base_model.updated_at)

    def test_two_saves(self):
        """Test whether consecutive saves of a BaseModel instance update its 'updated_at' attribute."""
        base_model = BaseModel()
        sleep(0.05)
        first_updated_at = base_model.updated_at
        base_model.save()
        second_updated_at = base_model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base_model.save()
        self.assertLess(second_updated_at, base_model.updated_at)

    def test_save_with_arg(self):
        """Test whether attempting to save a BaseModel instance with an argument raises a TypeError."""
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save(None)

    def test_save_updates_file(self):
        """Test whether saving a BaseModel instance updates the corresponding JSON file."""
        base_model = BaseModel()
        base_model.save()
        base_model_id = "BaseModel." + base_model.id
        with open("file.json", "r") as f:
            self.assertIn(base_model_id, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """Unit tests for the to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        """Test whether the to_dict method returns a dictionary."""
        base_model = BaseModel()
        self.assertTrue(dict, type(base_model.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test whether the dictionary returned by to_dict contains the correct keys."""
        base_model = BaseModel()
        self.assertIn("id", base_model.to_dict())
        self.assertIn("created_at", base_model.to_dict())
        self.assertIn("updated_at", base_model.to_dict())
        self.assertIn("__class__", base_model.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test whether to_dict includes attributes added after instantiation."""
        base_model = BaseModel()
        base_model.name = "Egerton"
        base_model.my_number = 98
        self.assertIn("name", base_model.to_dict())
        self.assertIn("my_number", base_model.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test whether datetime attributes in the dictionary are strings."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(str, type(base_model_dict["created_at"]))
        self.assertEqual(str, type(base_model_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test whether the output of to_dict matches the expected dictionary."""
        current_datetime = datetime.today()
        base_model = BaseModel()
        base_model.id = "123456"
        base_model.created_at = base_model.updated_at = current_datetime
        expected_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': current_datetime.isoformat(),
            'updated_at': current_datetime.isoformat()
        }
        self.assertDictEqual(base_model.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test whether the output of to_dict differs from the instance __dict__."""
        base_model = BaseModel()
        self.assertNotEqual(base_model.to_dict(), base_model.__dict__)

    def test_to_dict_with_arg(self):
        """Test whether attempting to call to_dict with an argument raises a TypeError."""
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.to_dict(None)


if __name__ == "__main__":
    unittest.main()

