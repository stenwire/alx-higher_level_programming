#!/usr/bin/python3
"""
Contains the to_json_string function
"""


import json
"""Import The json module"""


def to_json_string(my_obj):
    """"converts a string obj to json"""
    return json.dumps(my_obj)
