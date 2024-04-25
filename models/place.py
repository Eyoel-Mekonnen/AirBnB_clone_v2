#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"  
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    user_ = relationship("User", back_populates="place_", cascade="delete")
    reviews = relationship("Review", back_populates="place", cascade="delete")

    @getter
    def reviews(self):
        """returns list of reviews usin g filestorage"""
        from models import storage
        all_reviews = storage.all(Review)
        place_reviews = [review for review in all_reviews.values() if review.place_id == self.id]
        return place_reviews
