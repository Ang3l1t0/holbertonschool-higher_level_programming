#!/usr/bin/python3
"""print_square"""


def print_square(size):
    """print_square

    Arguments:
        size {int} -- square size

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is lower than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _i in range(size):
        print('#' * size)
