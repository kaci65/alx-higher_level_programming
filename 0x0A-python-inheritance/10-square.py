#!/usr/bin/python3
"""A class Square that inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines and instantiates a class"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of Square"""
        return self.__size * self.__size
