#!/usr/bin/python3
"""A class Student that defines some student property"""


class Student():
    """
    Definition of student class
    """
    
    def __init__(self, first_name, last_name, age):
        """Definition of students property"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict of obj"""
        return self.__dict__
