#!/usr/bin/python3
"""Function module"""


def is_same_class(obj, a_class):
    """ returns True if object is exactly an instance of the specified class;
    otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
