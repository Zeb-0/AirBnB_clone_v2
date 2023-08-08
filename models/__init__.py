#!/usr/bin/python3
"""
Package Initialization Script for the 'models' package.

This script initializes the 'models' package by importing essential classes
and setting up the FileStorage engine. It ensures proper configuration
for collaborative development and data storage.
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


storage = FileStorage()
storage.reload()
