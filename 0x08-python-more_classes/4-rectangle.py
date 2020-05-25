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

    def area(self):
        """Rectangle area

        Returns:
            int -- area of a rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """Rectangle perimeter

        Returns:
            int -- perimeter of a rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """Get string representation of rectangle
        """
        if self.height == 0 or self.width == 0:
            return ("")
        w = "#" * self.width
        printed = w
        for _i in range(self.height-1):
            printed += "\n" + w
        return (printed)

    def __repr__(self):
        """Get string evaluation of rectangle."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
