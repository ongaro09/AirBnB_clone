#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as a foundation
for other models within the AirBnB project.
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    The BaseModel class defines common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the BaseModel class.

        Attributes:
            id (str): Assigns a universally unique identification (id) to the object
            created_at (datetime): Assigns the current datetime when the instance is created
            updated_at (datetime): Assigns the current datetime when the instance is created
                and will be updated every time you change the object
        """
        if kwargs:
            for attribute, value in kwargs.items():
                if attribute == "created_at" or attribute == "updated_at":
                    setattr(self, attribute, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, attribute, value)
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of an instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the instance attribute updated_at with the current datetime."""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        return obj_dict

