#!/usr/bin/python3
"""
Module contains class Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A sub class of class Rectangle
    """

    def __init__(self, size):
        """
        Intialises the instance variable
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self, width, height)

    def area(self):
        """
        calculate area
        """

        return self.__width * self.__height
