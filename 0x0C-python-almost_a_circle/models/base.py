#!/usr/bin/python3
"""module for class Base"""
import json


class Base:
    """This class will be the “base” of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """assign the public instance attribute id with argument
        value. Otherwise, increment __nb_objects and assign the
        new value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
