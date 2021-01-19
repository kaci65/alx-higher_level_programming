#!/usr/bin/python3
"""Writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using
    a JSON representation
    """
    with open(filename, mode="w") as fd:
        fd.write(json.dumps(my_obj))
