#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstracted storage engine.

    Attributes:
        file_path (str): The name of the file to save objects to.
        objects (dict): A dictionary of instantiated objects.
    """
    file_path = 'file.json'
    objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.objects

    def new(self, obj):
        """Set obj in objects with key <obj_class_name>.id."""
        obj_class_name = obj.__class__.__name__
        FileStorage.objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize objects to the JSON file file_path."""
        objects_dict = FileStorage.objects
        objects_dict_serialized = {key: value.to_dict() for key,
                                   value in objects_dict.items()}
        with open(FileStorage.file_path, "w") as file:
            json.dump(objects_dict_serialized, file)

    def reload(self):
        """Deserialize the JSON file file_path to objects, if it exists."""
        try:
            with open(FileStorage.file_path) as file:
                objects_dict = json.load(file)
                for obj_data in objects_dict.values():
                    class_name = obj_data['__class__']
                    del obj_data['__class__']
                    self.new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            return
