#!/usr/bin/python3

"""
Module to divide a matrix by a given number
"""

def matrix_divided(matrix, div):
    """
    Divide a matrix by a given number and return the new matrix
    """

    if div == 0:
        raise ZeroDivisionError("division by zero is not allowed")

    check_matrix(matrix)

    return [[round(elem / div, 2) for elem in row] for row in matrix]


def check_matrix(matrix):
    """
    Validate the matrix to ensure only integers or floats are used and all rows have same length
    """

    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix should contain only numbers")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("all rows of the matrix should have the same size")


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    div = 2

    print(matrix_divided(matrix, div))
