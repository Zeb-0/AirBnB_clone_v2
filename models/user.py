#!/usr/bin/python3
""" Module containing the User class that inherits from BaseModel. """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class, representing users in the system,
    inherits from BaseModel. """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
