#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_mat = []
        for row in matrix:
            row = []
            for col in row:
                row.append(col ** 2)
            new_mat.append(row)
        return new_mat
