#!/usr/bin/python3
# encoding: utf-8
def add_integer(a, b=98):
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is int and type(b) is int:
        return a + b
    else:
        raise TypeError('a must be an integer or b must be an integer')
