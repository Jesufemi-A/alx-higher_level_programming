#!/usr/bin/python3
"""
This module divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    checks for validation and divide elemens in matrix

    parameter:
    matrix: list of list of type float or int
    div: divisor, must be an int or float

    return: a new list
    """

    new_matrix = []
    row_size =  set()

    if div == 0:
        raise ZeroDivisionError("division by Zero")
    elif isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif isinstance(matrix, list):
        for row in matrix:
            row_size = set(len(row))
        if len(row_size) != 1:
            raise TypeError("Each row of the matrix must have the same size")
        for row in matrix:
            if isinstance(row, list):
                for inner in row:
                    if isinstance(inner, (int, float)):
                        div_result =  round(inner / div, 2)
                        new_matrix.append(div_result)
                    else:
                        new_matrix.clear()
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
