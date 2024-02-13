#!/usr/bin/python3
"""This module defines the Review class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class represents a review for a place in the application."""
    place_id = ""
    user_id = ""
    text = ""
