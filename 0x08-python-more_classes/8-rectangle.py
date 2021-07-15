#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        w = str(self.print_symbol) * self.width
        printed = w
        for _i in range(self.height-1):
            printed += "\n" + w
        return (printed)

    def __repr__(self):
        """Get string evaluation of rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Action taken when instance is deleted
        """
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
            print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bigger or equal

        Arguments:
            rect_1 {Rectangle} -- rectangle 1
            rect_2 {Rectangle} -- rectangle 2

        Raises:
            TypeError: If rect_1 is not type Rectangle
            TypeError: If rect_2 is not type Rectangle

        Returns:
            Rectangle -- Returns the biggest rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        r_area1, r_area2 = rect_1.area(), rect_2.area()
        if r_area1 == r_area2:
            return rect_1
        elif r_area1 > r_area2:
            return rect_1
        else:
            rect_2
