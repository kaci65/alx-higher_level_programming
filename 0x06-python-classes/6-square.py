#!/usr/bin/python3
""""A class Square that defines a square: (based on 5-square.py)"""


class Square:
    """Defines a class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def size(self):
        return self.__position

    @position.setter
    def position(self, value):
        """incomplete code"""

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    """incomplete code"""
