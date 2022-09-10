#!/usr/bin/python3


"""
    Module that defines FileStorage class.
    It serializes instances to a JSON file and
    deserializes JSON file to instances.
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        FileStorage: FileStorage class
        Attributes:
            __file_path (str): string-path to the JSON file (ex.file.json)
            __objects (dict): mpty but will store all objects by
                <class name>.id (ex: to store a BaseModel objet with
                id=12121212, the key will be BaseModel.12121212)
            all(self): returns the dictionary __objects
            new(self, obj): sets in __objects the obj with key
                <obj class name>.id
            save(self): serializes __objects to the JSON file
                (path: __file_path)
            reload(self): deserializes the JSON file to __objects
                (only if the JSON file (__file_path) exists; otherwise, do
                nothing. If the file doesn't exist, no exception should be
                raised)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
        <obj_class_name>.id
        """
        ocname = obj.__class__.__name__

        # creating a key from concatenating class name and id
        # setting the key, value of the class __objects attribute
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        new = FileStorage.__objects
        obj_dict = {key: new[key].to_dict() for key in new.keys()}
        with open(FileStorage.__file_path, mode="w") as fp:
            json.dump(obj_dict, fp)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for k, v in objdict.items():
                    objdict = v
                    self.new(eval(objdict["__class__"])(**objdict))
        except FileNotFoundError:
            return
