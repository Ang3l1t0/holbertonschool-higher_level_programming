#!/usr/bin/python3
"""Student class

Returns:
    json -- dictionary representation of a Student instance
"""


class Student:
    """Class Student
    """

    def __init__(self, first_name, last_name, age):
        """initialize method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json method
        """
        return self.__dict__