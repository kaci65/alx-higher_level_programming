#!/usr/bin/python3
"""Append string to text file"""


def append_write(filename="", text=""):
    """function that appends string at the ed of text file (UTF8)
    and returns number of characters added
    """
    with open(filename, encoding="UTF-8", mode="a") as fd:
        return fd.write(text)
