#!/usr/bin/python3
""" This module defines the Place class. """

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    Attributes:
        city_id (str): City's ID to which the place belongs.
        user_id (str): User's ID who owns the place.
        name (str): Place's name.
        description (str): Place's description.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests in the place.
        price_by_night (int): Price per night for the place.
        latitude (float): Latitude coordinate of the place.
        longitude (float): Longitude coordinate of the place.
        amenity_ids (list): List of amenity IDs associated with the place.
        """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
