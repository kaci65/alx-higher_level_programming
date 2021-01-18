#!/usr/bin/python3
"""A class Rectangle that inherits from 7-base_geometry.py - task based on
8-rectangle.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines and instantiates a class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
