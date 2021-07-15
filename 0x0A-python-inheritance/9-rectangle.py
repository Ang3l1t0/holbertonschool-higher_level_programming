#!/usr/bin/python3
"""base geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class

    Arguments:
        BaseGeometry {class}
    """

    def __init__(self, width, height):
        """initialize

        Arguments:
            width {int} -- width
            height {int} -- height
        """
        self.__width = width
        self.__height = height
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)

    def area(self):
        """return area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
