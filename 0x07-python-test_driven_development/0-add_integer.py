#!/usr/bin/python3

"""
This module add two integers
"""


def add_integer(a, b=98):
    """
    This adds two value of type int
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if type(a) == float:
            a = int(a)
        if type(b) == float:
            b = int(b)
        return a + b
