#!/usr/bin/python3
""" This module defines Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits from BaseModel.
    Attributes:
        place_id (str): Place's ID to which the review belongs.
        user_id (str): User's ID who wrote the review.
        text (str): Review's text content. """
    place_id = ""
    user_id = ""
    text = ""
