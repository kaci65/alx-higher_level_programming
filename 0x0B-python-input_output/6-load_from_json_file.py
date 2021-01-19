#!/usr/bin/python3
"""Create Object from JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a "JSON file" """
    with open(filename, encoding="UTF-8") as fd:
        return json.load(fd)
