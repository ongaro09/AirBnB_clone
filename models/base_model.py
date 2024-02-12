#!/usr/bin/python3
"""
Defines the BaseModel class which serves as the foundation for other models
within the AirBnB project.
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Represents the BaseModel class, providing common attributes and methods
    for other classes in the AirBnB project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the BaseModel class.

        Attributes:
            id (str): A universally unique identification (ID) assigned to the object.
            created_at: Represents the timestamp of when the instance is created.
            updated_at: Represents the timestamp of when the instance is updated.
        """
        if kwargs is not None and kwargs != {}:
            for attribute in kwargs:
                if attribute == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif attribute == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[attribute] = kwargs[attribute]
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Returns a string representation of the instance """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the instance's 'updated_at' attribute with the current datetime """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Serializes the instance into a dictionary representation.

        Returns:
            dict: A dictionary containing all keys and values of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        return obj_dict

