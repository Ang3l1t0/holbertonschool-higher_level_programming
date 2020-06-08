#!/usr/bin/python3
"""Square class module
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square

    Args:
        Rectangle ([class]): class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize method

        Args:
            size ([int]): [size of square]
            x (int, optional): number of spaces. Defaults to 0.
            y (int, optional): number of \n. Defaults to 0.
            id ([int], optional): id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method

        Returns:
            str: Returns string info about this square.
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.width)
