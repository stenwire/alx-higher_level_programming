#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # new_mat = matrix.copy()
    new_mat = []
    for i in matrix:
        new_mat.append(list(map((lambda x: x*x), i )))   
    return new_mat
