#!/usr/bin/python3
def read_file(filename=""):
    
    # read the file
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        # output the file content
        print(content)
