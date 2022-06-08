#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for item in matrix:
        new_list = list(map((lambda x: x * x), item))
    return new_list
