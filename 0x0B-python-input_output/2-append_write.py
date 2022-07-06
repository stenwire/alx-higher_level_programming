#!/usr/bin/python3
"""
Contains the apppend_file function
"""


def append_write(filename="", text=""):
    """"write to and output a text file"""
    with open(filename, mode='a+', encoding='utf-8') as f:
        chars = f.write(text)
    return chars
