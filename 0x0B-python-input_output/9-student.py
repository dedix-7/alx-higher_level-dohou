#!/usr/bin/python3
"""
A class Student that defines a student
"""


class Student:
    """
    Module: class student
    """

    def __init__(self, first_name, last_name, age):
        """
        Method: The instantiation method, __init__
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method to_json
        """
        return self.__dict__
