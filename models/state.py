#!/usr/bin/python3
""" Module containing the State class which inherits from BaseModel. """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class, representing different states in the system,
    inherits from BaseModel."""
    name = ""
