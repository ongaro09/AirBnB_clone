#!/usr/bin/python3

"""This module defines the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This class defines the BaseModel of the current project."""

    def __init__(self, *args, **kwargs):
        """Establish a BaseModel instance.

        Argumentss:
            *args: Accepts any number of positional arguments.
            **kwargs: attributes passed as key/value pairs.
        """
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Set the 'updated_at' timestamp to the current date and time."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """Produce a string representation of the BaseModel
        object for display purposes."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
