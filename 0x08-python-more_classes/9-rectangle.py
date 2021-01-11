#!/usr/bin/python3
"""A class Rectangle that defines a rectangle: (based on 8-rectangle.py)"""


class Rectangle:
    """public class attribute, counting number of instances"""
    number_of_instances = 0

    """public class attribute, printing # symbol for rectangle"""
    print_symbol = "#"

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
                    rect.append(str(self.print_symbol))
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
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        # turning a rectangle into a square with equal width and height
        return cls(width=size, height=size)
