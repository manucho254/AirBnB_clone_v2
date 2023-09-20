#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime,
                        default=datetime.utcnow())
    updated_at = Column(DateTime,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if kwargs:
            if not kwargs.get('id'):
                self.id = str(uuid.uuid4())

            if kwargs.get('created_at'):
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
            if kwargs.get('updated_at'):
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
            if not kwargs.get('created_at'):
                self.created_at = datetime.now()

            if kwargs.get('created_at') and kwargs.get('updated_at'):
                self.updated_at = self.created_at
            else:
                self.updated_at = datetime.now()

            if kwargs.get('__class__'):
                del kwargs['__class__']

            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)

        # delete _sa_instance_state if in dictionary
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']

        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})

        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary

    def delete(self):
        """ delete the current instance from the storage """

        models.storage.delete(self)
