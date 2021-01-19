#!/usr/bin/python3
"""Write string to text file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, encoding="UTF-8", mode="w") as fd:
        return fd.write(text)
