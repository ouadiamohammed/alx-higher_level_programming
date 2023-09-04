#!usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Devides all elements of a matrix"""

    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError()
    if len(matrix) == 0 or ((not isinstance(matrix[0], list)) or
                            len(matrix[0]) == 0):
        raise TypeError(err)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if not all(isinstance(i, (int, float)) for i in matrix[0]):
        raise TypeError(err)
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return new_matrix
