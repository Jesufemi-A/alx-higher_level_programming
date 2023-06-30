#!/usr/bin/python3
"""
This is a module that define a class Square
has validationfor parameter size of class Square
size: size of the square
"""


class Square:
    """
    This is a class Square
    define the size of a square and has type and value validatio
    """

    def __init__(self, size=0):
        """
        A special method that initilize paramter size
        checks for validation too
        """

        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must >= 0')
        else:
            self.__size = size

    def area(self):
        """
        this public instance method returns current square area
        """

        return self.__size * self.__size
