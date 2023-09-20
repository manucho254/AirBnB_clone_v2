#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String, ForeignKey

from models.base_model import BaseModel, Base


association_table = Table('place_amenity', Base.metadata,
                          Column(String(60), 'place_id',
                                 ForeignKey('places.id'),
                                 primary_key=True),
                          Column(String(60), 'amenity_id',
                                 ForeignKey('amenities.id',
                                 primary_ky=True))
                          )


class Amenity(BaseModel, Base):
    """ Amenity class that defines amenities
    """
    __tablename__ = "amenities"
    name = Column(String(128))
    place_amenities = relationship("Place", secondary=association_table)
