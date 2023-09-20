#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String, ForeignKey

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """ Amenity class that defines amenities
    """
    __tablename__ = "amenities"
    name = Column(String(128))
