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

    def test_id(self):
        """ Test id """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_save(self):
        """ Test save method """
        bm1 = BaseModel()
        up1 = bm1.updated_at
        bm1.save()
        up2 = bm1.updated_at
        self.assertNotEqual(up1, up2)

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
