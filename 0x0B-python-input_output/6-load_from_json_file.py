#!/usr/bin/python3
"""
Contains the from_json_string function
"""


import json


def load_from_json_file(filename):
    """reads and output from a json file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        content = json.load(f)
        return (content)