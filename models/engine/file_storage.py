#!/usr/bin/python3
"""
This module contains the FileStorage class which handles the serialization
and deserialization of instances to and from a JSON format.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    This class handles the serialization and deserialization of instances
    to and from a JSON format.
    """

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """
        Returns a dictionary of available model classes.
        """
        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def all(self, cls=None):
        """
        Returns a dictionary of all instances if cls is None,
        otherwise returns instances of the specified class.
        """
        if cls is None:
            return self.__objects
        else:
            return {key: obj for key, obj in self.__objects.items()
                    if isinstance(obj, cls)}

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        new_serialized_obj = {
            "{}.{}".format(obj.__class__.__name__, obj.id): obj.to_dict()
            for obj in self.__objects.values()
        }

        with open(self.__file_path, "w") as f:
            json.dump(new_serialized_obj, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if file exists.
        """
        try:
            with open(self.__file_path, "r") as f:
                info = json.load(f)
                for key, value in info.items():
                    class_name, obj_id = key.split('.')
                    obj = self.classes()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it exists.
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

