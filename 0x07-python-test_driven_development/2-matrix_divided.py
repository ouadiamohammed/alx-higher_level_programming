#!usr/bin/python3
"""function that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """Devides all elements of a matrix"""


    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")



    new_matrix = []
    temp = []

    for row in matrix:
        for element in row:
           result = round(element / div, 2)
           temp.append(result)
        new_matrix.append(temp)

    return new_matrix
