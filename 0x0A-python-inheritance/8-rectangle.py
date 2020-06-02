#!/usr/bin/python3
"""base geometry
"""


class BaseGeometry:
    """BaseGeometry class
    """

    def area(self):
        """area function

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator function

        Raises:
            TypeError: name must be an integer
            ValueError: name must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
