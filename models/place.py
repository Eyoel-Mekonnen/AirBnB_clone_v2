#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))
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
    reviews__ = relationship("Review", back_populates="place", cascade="delete")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenities")

    @property
    def reviews(self):
        """returns list of reviews usin g filestorage"""
        from models import storage
        all_reviews = storage.all(Review)
        place_reviews = [review for review in all_reviews.values() if review.place_id == self.id]
        return place_reviews

    @property
    def amenities(self):
        """Return list of amenity id"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """Append id to the attribute"""
        if type(obj) is Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
