#!/usr/bin/python3
from constantly import ValueConstant


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False