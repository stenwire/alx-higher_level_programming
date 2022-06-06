#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 1
    for mat in matrix:
        for element in mat:
            if i < len(mat):
                print(end=' ')
            print("{:d}".format(element), end='')
            
        print()
