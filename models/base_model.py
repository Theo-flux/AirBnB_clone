#!/usr/bin/python3


""" Defines class BaseModel
that defines all common attributes/methods for other
classes
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ A representation of BaseModel class """

    def __init__(self, name="", my_number=0):
        """ An initialisation of class instance
        Args:
            my_number (int): integer variable
            name (str): string variable
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ String representation of class """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
