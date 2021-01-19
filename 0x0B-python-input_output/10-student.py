#!/usr/bin/python3
"""A class Student"""


class Student:
    """Defines class Student"""
    def __init__(self, first_name, last_name, age):
        """initialises class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student
        instance - same as 9-class_to_json.py
        """
        old_dict = self.__dict__
        new_dict = {}
        if attrs is None:
            return old_dict
        for key, value in old_dict.items():
            new_dict[key] = value
        return new_dict
