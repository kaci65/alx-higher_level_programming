#!/usr/bin/python3
"""Read text file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="UTF-8") as fd:
        print(fd.read(), end="")
