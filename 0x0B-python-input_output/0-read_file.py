#!/usr/bin/python3
"""
Contains the read_file function
"""


def read_file(filename=""):
    """""reads and output a text file"""
    # read the file
    with open(filename, mode="r", encoding='utf-8') as f:
        content = f.read()
        # output the file content
        print(content, end="")
