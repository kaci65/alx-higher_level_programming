#!/usr/bin/python3
"""A class Rectangle that defines a rectangle: (based on 0-rectangle.py)"""


class Rectangle:
    """Defines and instantiates a  class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """gets value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
