#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base()
"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """inherits from Base and links to mysql table states"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
