#!/usr/bin/python3
"""
A function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Module: class_to_json
    Returns: Builds a dictionary
    """
    return obj.__dict__
