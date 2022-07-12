#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""


def class_to_json(obj):
    """A function that returns the dictionary description  of a class object
    with simple data structure"""
    return obj.__dict__
