#!/usr/bin/python3
"""
contains the class definition of City and an inherits from Base(model_state)
"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """inherits from Base and links to mysql table cities"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False,)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
