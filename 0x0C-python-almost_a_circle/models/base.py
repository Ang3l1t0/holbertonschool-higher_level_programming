#!/usr/bin/python3
"""model Base"""
from json import dumps


class Base:
    """Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string method

        Args:
            list_dictionaries ([int]):  is a list of dictionaries

        Returns:
            [JSON]: Return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
