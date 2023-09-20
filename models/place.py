#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv

from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship

STORAGE = getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    if STORAGE == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity",
                                 secondary='place_amenity',
                                 backref='place_amenities',
                                 viewonly=False
                                 )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

    amenity_ids = []

    @property
    def reviews(self):
        """ The getter attribute for use with FileStorage """
        review_objs = []

        if STORAGE != 'db':
            from models import storage

            all_objs = storage.all()
            for obj in all_objs.items():
                a, b = obj
                if 'Review' in a and self.id in b:
                    review_objs.append(obj)

        return review_objs

    @property
    def amenities(self):
        """ Getter attribute amenities that returns
            the list of Amenity instances based on
            the attribute amenity_ids that contains
            all Amenity.id linked to the Place.
        """
        instances = []

        if STORAGE != 'db':
            from models import storage
            from model.amenity import Amenity

            objects = storage.all(Amenity)
            for _id in type(self).amenity_ids:
                for key, val in objects.items():
                    if val.id == _id:
                        instances.append(val)
        return instances

    @amenities.setter
    def amenities(self, obj):
        """ Setter attribute amenities that handles
            append method for adding an Amenity.id
            to the attribute amenity_ids
        """
        if STORAGE != 'db':
            from models.amenity import Amenity

            if not isinstance(obj, Amenity):
                return

            type(self).amenity_ids.append(obj.id)
