#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from models import storage
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Columns(DateTime, nullable=False, default=datetime.utcnow())
    update_at = Columns(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key != '__class__':
                    self.__dict__[key] = value
    

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = type(self).__name__
        if dictionary.get("_sa_instance_state"):
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        storage.delete(self)
