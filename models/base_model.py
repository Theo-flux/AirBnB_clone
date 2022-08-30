#!/usr/bin/python3


"""
    Module that defines BaseModel class
    which defines all common attributes/methods for the instances
"""


from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """
        BaseModel: BaseModel class
        Attributes:
                    id (int): instance id
                    updated_at (str): date/time of instance update
                    save(): updates the date/time of instance
                    to_dict(): create a dict of all the instance attributes
        Args:
            id: instance id
            created_at: instance creation date/time
            updated_at: instance updates date/time
        Raises:
    """

    def __init__(self, **kwargs):
        """ An initialisation of class instance """
        if kwargs is not None:
            for key, value in kwargs.items():
                if key is "created_at":
                    self.key = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key is "updated_at":
                    self.key = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key is "__class__":
                    continue
                else:
                    self.key = value
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def save(self):
        """
            Updates the public instance attribute with the current datetime
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
