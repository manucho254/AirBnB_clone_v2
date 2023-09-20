#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["city_id"] = "some_id"
        new = self.value(**_dict)

        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["user_id"] = "some_id"
        new = self.value(**_dict)

        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["name"] = "test"
        new = self.value(**_dict)

        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["description"] = "test"
        new = self.value(**_dict)

        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["number_rooms"] = 10
        new = self.value(**_dict)

        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["number_bathrooms"] = 30
        new = self.value(**_dict)

        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["max_guest"] = 50
        new = self.value(**_dict)

        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["price_by_night"] = 100
        new = self.value(**_dict)

        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["latitude"] = 4.2
        new = self.value(**_dict)

        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["longitude"] = 5.2
        new = self.value(**_dict)

        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        _dict = new.to_dict()
        _dict["amenity_ids"] = []
        new = self.value(**_dict)

        self.assertEqual(type(new.amenity_ids), list)
