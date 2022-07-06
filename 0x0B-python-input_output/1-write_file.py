#!/usr/bin/python3
def write_file(filename="", text=""):
    chars = 1
    # open file to write
    with open(filename, mode='w+', encoding='utf-8') as f:
        f.write(text)
    # loop through file content
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        for lines in content:
            chars+=1
    # output nmba of chars
    return chars
