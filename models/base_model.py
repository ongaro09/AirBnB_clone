#!/usr/bin/python3
"""
Custom base class for the AirBnB clone project
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Custom base class serving as the foundation for all classes in the AirBnB clone project

    Attributes:
        id(str): unique identifier for each instance
        created_at: indicates the datetime when the instance was created
        updated_at: indicates the datetime when the instance was last updated

    Methods:
        __str__: returns a string representation of the instance
        save(self): updates the 'updated_at' attribute with the current datetime
        to_dict(self): returns a dictionary containing the instance attributes

    """

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes either from provided kwargs or generates new values

        Args:
            *args(args): positional arguments
            **kwargs(dict): keyword arguments representing attribute values

        """
        DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all instance attributes
        """
        obj_dict = {}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
