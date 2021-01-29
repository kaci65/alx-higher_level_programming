#!/usr/bin/python3
"""module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overrides the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def to_dictionary(self):
        """Returns a dict representation of Square"""
        keys = ['id', 'size', 'x', 'y']
        new_dict = {}
        for key in keys:
            new_dict[key] = getattr(self, key)
        return new_dict
