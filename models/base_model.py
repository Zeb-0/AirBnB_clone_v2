#!/usr/bin/python3
""" This module defines the BaseModel class. """
from datetime import datetime
from uuid import uuid4
import models
""" import moduls """


class BaseModel:
    """  BaseModel class for common attributes/methods.
    Attributes:
        id (str): Unique identifier of the instance.
        created_at (datetime): Date and time of creation.
        updated_at (datetime): Date and time of last update. """

    def __init__(self, *args, **kwargs):
        """" constructor with public instance attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ method that define print """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ method that updates the public instance attribute updated_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ method that returns a dictionary containing all keys/values of
        __dict__ of the instance """
        attribute_dict = self.__dict__.copy()
        attribute_dict['__class__'] = self.__class__.__name__
        attribute_dict['created_at'] = self.created_at.isoformat()
        attribute_dict['updated_at'] = self.updated_at.isoformat()
        return(attribute_dict)
