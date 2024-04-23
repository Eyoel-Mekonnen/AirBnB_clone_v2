#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models."""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""

        dict_repr = self.to_dict()
        dict_repr.pop('__class__', None)
        return f"[{type(self).__name__}] ({self.id}) {dict_repr}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def datetime_format(self, dt):
        """ Returns expected output style. """
        if dt is None:
            return None
        return f"datetime.datetime({dt.year}, {dt.month}, {dt.day},
                                   {dt.hour}, {dt.minute}, {dt.second})"

    def to_dict(self):
        """Convert instance into dict format"""
        """ class_name_ = self.__class__.__name__i"""
        """dict_name = {"__class__": class_name_}"""
        dict_repr = {}
        for key, value in self.__dict__.items():
            if key == '_sa_instance_state':
                continue
            if isinstance(value, datetime):
                dict_repr[key] = self.datetime_format(value)
            else:
                dict_repr[key] = value
        dict_repr['__class__'] = type(self).__name__
        return dict_repr

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
