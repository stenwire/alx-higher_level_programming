#!/usr/bin/python3
"""
A class Student that defines some student property
"""


class Student():
    """Definition of student clas"""
    def __init__(self, first_name, last_name, age):
        """Definition of students property"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation 
        of a Student instance for given attrs"""
        if attrs is not None:
            my_dict = {}
            for i in attrs:
                try:
                    my_dict[i] = self.__dict__[i]
                except KeyError:
                    pass
            return my_dict
        return self.__dict__
