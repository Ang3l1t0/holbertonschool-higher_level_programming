#!/usr/bin/python3
"""Square class"""


class Square:
    """define size
    Arguments:
        size: size of a square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of square"""
        return self.__size ** 2

    def my_print(self):
        square_list = []
        for i in range(self.__size):
            square_list.append('#' * self.__size)
        print(*square_list, sep="\n")

    @property
    def size(self):
        """getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
