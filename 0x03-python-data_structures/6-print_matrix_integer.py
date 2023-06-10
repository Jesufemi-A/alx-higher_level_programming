#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for outer in range(len(matrix)):
        for inner in range(len(matrix[outer])):
            if inner != 0:
                print(" ", end="")
            print("{:d}".format(matrix[outer][inner]),  end="")
        print()
