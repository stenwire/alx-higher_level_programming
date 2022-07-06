#!/usr/bin/python3
"""
This module adds all argument from the cmd line to a list,
and then saves them to a json file
"""


from sys import argv
"""Importing The argv mwthod from sys module"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file



filename = "add_item.json"

try:
    content = load_from_json_file(filename)
except:
    content = []

for i in range(1, len(argv)):
    content.append(argv[i])

save_to_json_file(content, filename)
