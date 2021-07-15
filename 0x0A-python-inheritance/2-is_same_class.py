#!/usr/bin/python3
"""Is same class
"""


def is_same_class(obj, a_class):
    """is same class

    Arguments:
        obj {} -- [input object]
        a_class {} -- [type class to be compared]

    Returns:
        [type] -- [description]
    """
    if type(obj) is a_class:
        return True
    else:
        return False
