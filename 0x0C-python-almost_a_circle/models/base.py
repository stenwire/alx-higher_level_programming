#!/usr/bin/python3
"""
This module contains the "Base" class
"""

import json


class Base:
    """A base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        my_list = []
        if list_objs is not None:
            for i in list_objs:
                my_list.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns a converted json"""
        if json_string is not None:
            return [json.loads(json_string)]
        return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        my_list = []
        try:
            with open(filename, 'r') as f:
                my_list = cls.from_json_string(f.read())
            for i, e in enumerate(my_list):
                my_list[i] = cls.create(**my_list[i])
        except:
            pass
        return my_list
