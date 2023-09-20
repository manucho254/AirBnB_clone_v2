#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 ForeignKey('places.id'),
                                 primary_key=True),
                          Column('amenity_id',
                                 ForeignKey('amenities.id'),
                                 primary_key=True)
                          )


class Amenity(BaseModel, Base):
    """ Amenity class that defines amenities
    """
    __tablename__ = "amenities"
    name = Column(String(128))
    place_amenities = relationship("Place",
                                   back_populates="places",
                                   secondary=association_table)
