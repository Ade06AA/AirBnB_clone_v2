#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models import StorageType
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if StorageType == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """doc"""
            from models import storage
            newl = []
            newd = storage.all(City)
            for i in newd.values():
                if i.state_id == self.id:
                    newl.append(i)
            return newl
