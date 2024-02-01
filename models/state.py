#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a class State in a MySQL database.

    Inherits from SQLAlchemy and links to the MySQL table `states`.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store states.
        name (sqlalchemy String): The name of the state.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all cities in the state."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id = self.id:
                    city_list.append(city)
            return city_list