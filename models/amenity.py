#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from models import StorageType
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if StorageType == "db":
        name = Column(String(128), nullable=False)
        places_amenities = relationship("Place",
                                        secondary=place_amenity,
                                        back_populates='amenities')
    else:
        name = ""
