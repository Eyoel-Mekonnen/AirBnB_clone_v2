#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
import models
from os import getenv


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models."""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if len(kwargs) != 0:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if (key == "__class__"):
                    continue
                elif (key == "created_at"):
                    if isinstance(value, str):
                        date_object = datetime.strptime(value, time_format)
                        setattr(self, key, date_object)
                    else:
                        setattr(self, key, value)
                elif (key == "updated_at"):
                    if isinstance(value, str):
                        date_object = datetime.strptime(value, time_format)
                        setattr(self, key, date_object)
                    else:
                        setattr(self, key, value)
                else:
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def date_time_format(self, dt):
        """Convert to datetiem object"""
        if dt is None:
            return None

        return "datetime.datetime({}, {}, {}, {}, {}, {})".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    def __str__(self):
        """Returns a string representation of the instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        #print("I am at save in basemodel")
        self.updated_at = datetime.now()
        models.storage.new(self)
        #print("I ma saved as new")
        models.storage.save()
        #print("I am finally saved")

    def to_dict(self):
        """Convert instance into dict format"""
        dict_name = {}
        for key, value in self.__dict__.copy().items():
            if (key != '_sa_instance_state'):
                dict_name[key] = value
            if getenv("HBNB_TYPE_STORAGE") != "db":
                if '_sa_instance_state' in self.__dict__.keys():
                    del self.__dict__['_sa_instance_state']
                if isinstance(value, datetime):
                    dict_name[key] = value.isoformat()
        return dict_name

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
