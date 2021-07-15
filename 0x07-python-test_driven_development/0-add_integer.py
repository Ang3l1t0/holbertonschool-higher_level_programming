#!/usr/bin/python3
"""add_integer - sum of two variables"""


def add_integer(a, b=98):
    """add_integer - sum of two variables

    Arguments:
        a {int} -- First value

    Keyword Arguments:
        b {int} -- Second value (default: {98})

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
    Returns:
        int -- sum of two values
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    return (a + b)
