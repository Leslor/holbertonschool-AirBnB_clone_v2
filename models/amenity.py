#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.place import place_amenity
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """"Amenity model"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""
