#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        for item in matrix:
            return list(map((lambda x: x*x), item))
