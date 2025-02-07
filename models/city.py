#!/usr/bin/python3
""" City Module for HBNB project """
import os

from sqlalchemy import Column, String, ForeignKey

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"))
    else:
        name = ""
        state_id = ""
