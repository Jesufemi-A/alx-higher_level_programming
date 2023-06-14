#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    c_matrix = matrix[:]

    def square(value):
        return value ** 2

    c_matrix = list(map(square, c_matrix))
    return c_matrix
