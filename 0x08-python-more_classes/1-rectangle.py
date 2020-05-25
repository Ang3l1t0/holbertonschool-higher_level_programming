#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """Rectangle class
    """
    def __init__(self, width=0, height=0):
        """initialize class
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    # width
    @property
    def width(self):
        """get width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # heigth
    @property
    def height(self):
        """get width of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
