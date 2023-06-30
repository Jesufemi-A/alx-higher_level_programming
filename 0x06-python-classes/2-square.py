#!/usr/bin/python3
"""
This is a module that defines a class square
"""


class Square:
    """
    This class defines a square
    has a private instance attribute __size
    """

    def __init__(self, size=0):
        """
        This is a special method that intialises the attributes
        has type and valiue validation
        """

        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
