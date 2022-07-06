#!/usr/bin/python3
"""
Contains the from_json_string function
"""


import json
"""Importing The json module"""


def save_to_json_file(my_obj, filename):
    """converts a string obj to json"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
