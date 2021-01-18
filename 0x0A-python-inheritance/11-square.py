#!/usr/bin/python3
"""A class Square that inherits from Rectangle (9-base_geometry.py) - task
based on 10-square.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines and instantiates a class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of Square"""
        return self.__size * self.__size

    def __str__(self):
        """returns the rectangle description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
