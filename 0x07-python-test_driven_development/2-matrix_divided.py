#!/usr/bin/python3
"""Divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """function to divide elements"""
    """check if row is list"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        """check if matrix consists of numbers only"""
        for j in row:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

        """check size/length of row"""
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    """check div"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """check if div is zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """divide matrix"""
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
