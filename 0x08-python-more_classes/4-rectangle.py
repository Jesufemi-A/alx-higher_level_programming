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
        to set private attribute
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must >= 0')
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

    def print(self):
        """
        to print a rectangle
        with the character #
        """

        for i in range(self.height):
            for j in range(self.width):
                print('#', end='')
            if i != (self.height - 1):
                print()
            else:
                continue

    def __str__(self):
        """
        helper function for str
        """

        if self.width == 0 or self.height == 0:
            return ""
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print('#', end='')
                if i != (self.height - 1):
                    print()
                else:
                    continue
            return ""

    def __repr__(self):
        """
        helper function for repr
        to recreate a new instance by using eval()
        """

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
