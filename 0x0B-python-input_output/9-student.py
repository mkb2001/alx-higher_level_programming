#!/usr/bin/python3

"""
Student to JSON
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of Student object"""
        return self.__dict__
