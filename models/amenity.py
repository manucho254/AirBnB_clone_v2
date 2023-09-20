#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True)
                          )


class Amenity(BaseModel, Base):
    """ Amenity class that defines amenities
    """
    __tablename__ = "amenities"
    name = Column(String(128))
    place_amenities = relationship("Place",
                                   backref='amenities',
                                   secondary=place_amenity)
