#!/usr/bin/python3


""" Defines class BaseModel
that defines all common attributes/methods for other
classes
"""


from uuid import uuid4
from datetime import datetime
import json

class BaseModel:
    """ A representation of BaseModel class """

    def __init__(self, name="", my_number=0):
        """ An initialisation of class instance
        Args:
            my_number (int): integer variable
            name (str): string variable
        """
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def save(self):
        """ Updates the public instance attribute
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
        of the instance
        """
        toDict = self.__dict__
        toDict["created_at"] = self.created_at.isoformat()
        toDict["updated_at"] = self.updated_at.isoformat()
        toDict["__class__"] = self.__class__.__name__
        return toDict

    def __str__(self):
        """ String representation of class """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)
