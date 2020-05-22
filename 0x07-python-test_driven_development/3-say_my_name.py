#!/usr/bin/python3
"""say_my_name"""


def say_my_name(first_name, last_name=""):
    """say_my_name - print my name is...

    Arguments:
        first_name {str} -- first argument

    Keyword Arguments:
        last_name {str} -- second argument (default: {""})

    Raises:
        TypeError: If first name is not a string
        TypeError: If last name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
