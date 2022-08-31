#!/usr/bin/python3


"""
    Module that defines BaseModel class
    which defomes all common attributes/methods for the instances
"""


from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
        BaseModel: BaseModel class
        Attributes:
                    id (uuid4): instance id
                    updated_at (str/datetime): date/time of instance update
                    save(): updates the date/time of instance
                    to_dict(): create a dict of all the instance attributes
        Args:
            id: instance id
            created_at: instance creation date/time
            updated_at: instance updates date/time
        Raises:
    """

    def __init__(self, *args, **kwargs):
        """ An initialize a new BaseModel
            Args:
                *args (any): Unused.
                **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
        # if kwargs is given then update the attributes
        if kwargs:
            # temp variable to hold date/time i.e to comply with pycodestyle
            temp1 = kwargs.get("created_at")
            temp2 = kwargs.get("updated_at")
            self.id = kwargs.get("id")
            # Iso_format_string - '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(temp1, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(temp2, '%Y-%m-%dT%H:%M:%S.%f')
            # Only to be added if name/my_number is specified
            if kwargs.__contains__("name"):
                self.name = kwargs.get("name")
            if kwargs.__contains__("my_number"):
                self.my_number = kwargs.get("my_number")
        else:        
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        toDict = self.__dict__.copy()
        toDict["created_at"] = self.created_at.isoformat()
        toDict["updated_at"] = self.updated_at.isoformat()
        toDict["__class__"] = self.__class__.__name__
        return toDict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)
