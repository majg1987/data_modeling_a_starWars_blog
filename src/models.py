import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    email = Column(String(200), unique = True, nullable = False)
    password = Column(String(20), unique = True, nullable = False)
    favourites = relationship('Favourites', backref = 'User')


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key = True)
    name = Column(String(250), unique = True, nullable = False)
    gender = Column(String(20), nullable = False)
    birth_date = Column(String(10), nullable = False)
    height = Column(Integer, nullable = False)
    hair_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable = False)
    skin_color = Column(String(50), nullable = False)
    url_image = Column(String(200), unique = True, nullable = False, )
    description = Column(String(1000), unique = True, nullable = False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicles = relationship('Vehicles', backref = 'character')

class Planet(Base):
    __tablename__= 'planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), unique = True, nullable = False)
    population = Column(Integer, nullable = False)
    terrain = Column(String(50), nullable = False)
    climate = Column(String(50), nullable = False)
    orbit_period = Column(Integer, nullable = False)
    orbit_rotation = Column(Integer, nullable = False)
    diameter = Column(Integer, nullable = False)
    url_image = Column(String(200), unique = True, nullable = False)
    description = Column(String(1000), unique = True, nullable = False)
    character = relationship('Character', backref = 'planet')
    vehicles = relationship('Vehicles', backref = 'planet')


class Vehicles(Base):
    __tablename__='vehicles'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), unique = True, nullable = False)
    model = Column(String(100), nullable = False)
    vehicle_class = Column(String(100), unique = True, nullable = False)
    passengers = Column(Integer, nullable = False)
    max_speed = Column(Integer, nullable = False)
    consumables = Column(Integer, nullable = False)
    url_image = Column(String(200), unique = True, nullable = False)
    description = Column(String(1000), unique = True, nullable = False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))




    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')