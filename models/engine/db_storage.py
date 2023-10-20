#!/usr/bin/python3:x
""" module for new database storage.
"""

import os

from models.base_model import Base
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

ENV = os.getenv('HBNB_ENV')  # current environment
DB_USER = os.getenv('HBNB_MYSQL_USER')  # database user
DB_PASSWORD = os.getenv('HBNB_MYSQL_PWD')  # database password
DB_HOST = os.getenv('HBNB_MYSQL_HOST')  # database host
DB_NAME = os.getenv('HBNB_MYSQL_DB')  # database name
STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE')  # type of storage


class DBStorage:
    """ class DBStorage that defines database strorage
        Atrributes:
                   __engine: engine we use
                   __session: sqlalchemy session
    """
    __engine = None
    __session = None

    def __init__(self) -> None:
        """ intialize class
        """
        my_db = ('mysql+mysqldb://{}:{}@{}:3306/{}'
                 .format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
                 )
        # create engine
        self.__engine = create_engine(my_db, pool_pre_ping=True)

        if ENV == "test":

            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None) -> dict:
        """ query on the current database session
            (self.__session) all objects depending
            of the class name (argument cls).
            Args:
                cls: class object
        """

        classes = [User, State, City, Amenity, Place, Review]
        data = []
        objects = {}
        class_name = None

        if cls is None:
            for obj in classes:
                objs = self.__session.query(obj).all()
                data.extend(objs)
        else:
            data.extend(self.__session.query(cls).all())

        for obj in data:
            class_name = obj.__class__.__name__
            key = "{}.{}".format(class_name, obj.id)
            objects[key] = obj

        return objects

    def new(self, obj):
        """ add the object to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database
            session obj if not None.
            Args:
                obj: class object
        """

        if obj is None:
            return

        self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        # scoped session
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ method def close(self):: call remove()
            method on the private session attribute
            (self.__session) tips or close() on the class Session
        """

        self.__session.close()
