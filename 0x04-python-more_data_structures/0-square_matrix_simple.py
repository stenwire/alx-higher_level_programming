#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        new_mat = list(map((lambda x: x*x), i ))   
    return new_mat
