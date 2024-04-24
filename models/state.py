#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column, Integer
from models.city import City
from sqlalchemy.ext.declarative import declarative_base

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities_ = relationship("City", back_populates="state", cascade="delete")

    @property
    def cities(self):
        """Return list of city where state_id current state_id"""
        dict_objects = models.storage.all(City)
        list_city = []
        for key, value in dict_objects.items():
            if self.id == value.state_id:
                list_city.append(value)
        return list_city
