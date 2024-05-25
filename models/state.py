#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column, Integer
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
import models
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """Return list of city where state_id current state_id"""
        from models import storage
        from models.city import City
        all_cities = models.storage.all(City)
        return [city for city in storage.all(City).values()
                if city.state_id == self.id]
