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

    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              backref='state',
                              cascade='all, delete')
    else:
        name = ""

    @property
    def cities(self):
        """ function that returns
            all cities related to state
        """

        cities_arr = []
        models.storage.reload()
        objects = models.storage.all(City)

        for val in objects.values():
            if self.id == val.state_id:
                cities_arr.append(val)

        return cities_arr
