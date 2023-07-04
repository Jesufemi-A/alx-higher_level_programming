#!/usr/bin/python3
"""
This module has a function that print square
square is printed with character #
"""

def print_square(size):
    """
    This function print square with character #

    parameter:
    size(int): character #
    """

    if isinstance(size, (float)) and size < 0:
        raise TypeError('size must be an integer')
    elif not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
