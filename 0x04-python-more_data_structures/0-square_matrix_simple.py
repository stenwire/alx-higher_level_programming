#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_mat = []
        for row in matrix:
            row_mat = []
            for i in row:
                row_mat.append(i ** 2)
            new_mat.append(cln)
        return new_mat
