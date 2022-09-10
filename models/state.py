#!/usr/bin/python3


"""
    Module that defines State class. It defines all
    common attributes/methods for state. Inherits from
    BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
        State: State class
        Attributes:
                    name (str): instance name
        Raises:
    """

    name = ""

