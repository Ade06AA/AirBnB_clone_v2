#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import StorageType
from sqlalchemy import Column, ForeignKey, String, Float, Integer, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id',
                             String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if StorageType == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review',
                               cascade="all, delete", backref="place")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='places_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """doc"""
            newl = []
            newd = storage.all(Reviews)
            for i in newd.values():
                if i.place_id == self.id:
                    newl.append(i)
            return newl

        @property
        def amenities(self):
            """doc"""
            newl = []
            newd = storage.all(amenities)
            for i in newd.values():
                if i.id in self.amenity_ids:
                    newl.append(i)
            return newl

        @amenities.setter
        def amenities(self, OVal):
            """doc"""
            if type(OVal) == Amenity:
                self.amenity_ids.append(OVal.id)
