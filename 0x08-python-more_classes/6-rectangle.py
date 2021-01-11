#!/usr/bin/python3I
"""A class Rectangle that defines a rectangle: (based on 5-rectangle.py)"""


class Rectangle:
    # public class attribute, counting number of instances
    number_of_instances = 0

    """Defines and instantiates a  class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        # gets value of width
        return self.__width

    @width.setter
    def width(self, value):
        # sets value of width
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        # gets value of height
        return self.__height

    @height.setter
    def height(self, value):
        # sets value of height
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        # if width or height is zero, perimeter equals zero

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints rectangle using # symbol"""
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for col in range(self.__height):
                for row in range(self.__width):
                    rect.append("#")
                if col < self.__height - 1:
                    rect.append("\n")
            rect = "".join(rect)
            return rect

    def __repr__(self):
        """
        returns a string representation of the rectangle so as
        to recreate a new instance by using eval()
        """
        new_rect = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return new_rect

    def __del__(self):
        """prints text when an instance of Rectangle is deleted"""
        print("Bye rectanIgle...")
        Rectangle.number_of_instances -= 1
