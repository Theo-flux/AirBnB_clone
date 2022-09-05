#!/usr/bin/python3


"""
    Module that defines User class that defines
    all common attributes/methods for user
"""


from models.base_model import BaseModel
 

class User(BaseModel):
    """
        User: User class
        Attributes:
                    email (str): instance email
                    password (str): instance password
                    first_name (str): instance first_name
                    last_name (str): instance last_name
         Raises:
     """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
