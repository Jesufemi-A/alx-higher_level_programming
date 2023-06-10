#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for outer in matrix:
        for inner in matrix:
            print("{:d}".format(inner),  end=" ")
