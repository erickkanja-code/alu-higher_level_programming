#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_i = []
        for x in i:
            new_i.append(x ** 2)
        new_matrix.append(new_i)
    return new_matrix
