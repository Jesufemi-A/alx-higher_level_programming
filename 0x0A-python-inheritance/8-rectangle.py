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
        super().integer_validator("width", width)
        super().integer_validator("height", width)
        self.__width = width
        self.__height = height
