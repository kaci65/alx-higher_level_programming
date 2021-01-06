#!/usr/bin/python3
class Square:
    """A class Square that defines a square: (based on 5-square.py)"""
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

    """incomplete code"""
