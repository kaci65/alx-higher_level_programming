#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_square_matrix = []
    for i in matrix:
        new_square_matrix.append(list(map(lambda x: x * x, i)))
    return new_square_matrix
