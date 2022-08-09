#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
import models
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ Class Place """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False,)
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Getter attribute that 
            returns a list of Review instances
            with place_id equals to the current Place.id """
            return list(filter(
                    lambda x: x.place_id == self.id , models.storage.all(
                    models.Review).values()))
    #city_id = ""
    #user_id = ""
    #name = ""
    #description = ""
    #number_rooms = 0
    #number_bathrooms = 0
    #max_guest = 0
    #price_by_night = 0
    #latitude = 0.0
    #longitude = 0.0
    #amenity_ids = []
