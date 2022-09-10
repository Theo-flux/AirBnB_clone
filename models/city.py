#!/usr/bin/python3


"""
    Module that defines City class. It defines all
    common attributes/methods for state. Inherits from
    BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
        City: City class
        Attributes:
                    name (str): instance name
                    state_id (str): instance state_id
        Raises:
    """

    name = ""
    state_id = ""

