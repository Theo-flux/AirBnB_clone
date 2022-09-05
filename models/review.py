#!/usr/bin/python3


"""
    Module that defines Review class. It defines all
    common attributes/methods for state. Inherits from
    BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review: Review class
        Attributes:
                    place_id (str): instance of place id
                    user_id (str): instance of user id
                    text (str): instance text
        Raises:
    """
    
    place_id = ""
    user_id = ""
    text = ""
