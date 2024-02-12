#!/usr/bin/python3
"""Module containing the City class that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a city, inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

