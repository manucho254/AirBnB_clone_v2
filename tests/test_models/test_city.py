#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest

import os

STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        dict_ = new.to_dict()
        dict_['state_id'] = "some_id"
        new = self.value(**dict_)

        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        dict_ = new.to_dict()
        dict_['state_id'] = "some_id"
        dict_['name'] = "kanairo"
        new = self.value(**dict_)

        self.assertEqual(type(new.name), str)
