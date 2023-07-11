#!/usr/bin/python3
"""
A module containing a subclass
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A sub class inheriting from Baseclass
    """

    def __init__(self, width, height):
        """
        This intializes the instance attributes
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate area
        """

        return self.__width * self.__height

    def __str__(self):
        """
        return rectangle
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
