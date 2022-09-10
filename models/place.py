#!/usr/bin/python3


"""
    Module that defines Place class. It defines all
    common attributes/methods for state. Inherits from
    BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
        Place: Place class
        Attributes:
                    name (str): instance name
                    city_id (str): instance city id
                    user_id: (str): instance state id
                    description (str): instance description
                    number_rooms (int): instance number of rooms
                    max_guest (int): instance maximum guest
                    number_bathrooms (int): instance number of bathrooms
                    price_by_night (int): instance of price by ight
                    latitude (float): instance of latitude
                    longitude (float): instance of longitude
                    amenity_ids (list): instance of lists of amenities
        Raises:
    """

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    number_bathrooms = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

