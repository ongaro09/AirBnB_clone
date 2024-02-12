#!/usr/bin/python3
"""Module containing the User class inheriting from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """Representation of a user that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

