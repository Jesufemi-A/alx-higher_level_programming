#!/usr/bin/python3
"""
Module contain class Rectangle
"""


class Rectangle:
    """
    define a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        magic method that initialises
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieve private attribute
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        set the private attribute
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
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        return area of rectangle
        """

        return self.width * self.height

    def perimeter(self):
        """
        return perimeter of rectangle
        """

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
