#!/usr/bin/python3
"""Initialize the file storage engine for the HBnB application.

This script initializes the file storage engine by
instantiating the FileStorage
class from the models.engine.file_storage module.
It also reloads any previously
saved data into memory.

Attributes:
    storage: An instance of the FileStorage class
    representing the storage engine
    for the HBnB application.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
