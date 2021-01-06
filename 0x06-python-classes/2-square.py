#!/usr/bin/python3
class Square:
    """A class Square that defines a square: (based on 1-square.py)"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
