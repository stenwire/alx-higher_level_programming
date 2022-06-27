#!/usr/bin/python3
# encoding: utf-8
"""
Name of modle: 4-print_square.py

This module contains one function print_square()
"""


def print_square(size):
    """Prints a square of '#' character(s)

    Args:
        size (int): size of square

    Returns:
        Nothing
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ZeroDivisionError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    i = 0
    while i < size:
        i+=1
        print('#'*size)
