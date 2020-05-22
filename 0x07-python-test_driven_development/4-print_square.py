#!/usr/bin/python3
"""print square"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _i in range(size):
        print('#' * size)
