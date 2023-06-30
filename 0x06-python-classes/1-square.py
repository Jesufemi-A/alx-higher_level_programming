#!/usr/bin/python3
"""
a class with private instance attribute - size
"""


class Square:
    """
    class with private instance attribute, size
    """
    def __init__(self, size):
        """
        special method for initialising attrihutes
        """

        self.__size = size


sq = Square(size)
