#!/usr/bin/python3
"""
Module contains class Rectangle
"""


class Rectangle:
    """
    This class contains getter amd setter method
    """

    def __init__(self, width=0, height=0):
        """
        the magic methof that intialises

        Args:
        width(int): must be an integer and greater than 0
        height(int): must be an integer and greater than 0
        """

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        """
        to retrieve private attribute
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        to set private instance attribute
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        retrieve private instance attribute
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        to set private instance attribute
        """

        if not isinstance(value, int):
            raise TypeError('Height must be an integer')
        elif value < 0:
            raise ValueError('Height must be >= 0')
        else:
            self_height = value
