#!/usr/bin/python3
"""Inherits
"""


def inherits_from(obj, a_class):
    """inherits_from

    Arguments:
        obj
        a_class

    Returns:
        bol -- true or false
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
