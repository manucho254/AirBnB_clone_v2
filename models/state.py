#!/usr/bin/python3
""" State Module for HBNB project """

import os

from models.city import City
from models.base_model import BaseModel, Base
import models

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128))
    cities = relationship('City',
                          backref='state',
                          cascade='all, delete')

    @property
    def cities(self):
        """ function that returns
            all cities related to state
        """
        if STORAGE != "db":
            objects = models.storage.all()
            cities_arr = []

            for obj in objects:
                if isinstance(obj, City):
                    if self.id == obj.state_id:
                        cities_arr.append(obj)

            return cities_arr
