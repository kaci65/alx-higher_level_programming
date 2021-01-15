#!/usr/bin/python3
"""Printing a square"""


def print_square(size):
    """function to print a square using # character"""
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
