#!/usr/bin/python3

"""
    This module is the file for Base Model:
        Attrs:
            id
            created_at
            updated_at
        Methods:
            save()
            to_dict()
"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """ Test cases """
    bm1 = BaseModel()
    bm2 = BaseModel()
    up1 = bm1.updated_at
    bm1.save()
    up2 = bm1.updated_at

    def test_isinstance(self):
        """ Test isinstance of BaseModel """
        self.assertIsInstance(self.bm1, BaseModel)

    def test_id_present(self):
        """ Test if id attr is present """
        self.assertTrue(hasattr(self.bm1, "id"))

    def test_id_uniqueness(self):
        """ Test if two instance id is not equal """
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_id_isstr(self):
        """ Test if id is a string """
        self.assertIsInstance(self.bm1.id, str)

    def test_save(self):
        """ Test save method """
        self.assertNotEqual(self.up1, self.up2)

    def test_to_dict(self):
        """ Test to_dict method """
        bm1 = BaseModel()
        bm1.name = "My First Model"
        bm1.my_number = 89
        bm_json = bm1.to_dict()
        self.assertIn('name', bm_json)
        self.assertIn('my_number', bm_json)
        self.assertIn('created_at', bm_json)
        self.assertIn('updated_at', bm_json)
        self.assertIn('__class__', bm_json)
        self.assertIsInstance(bm_json, dict)
