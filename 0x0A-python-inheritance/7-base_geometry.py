#!/usr/bin/python3
"""
Contains BaseGeometry Class
Updating BaseGeometry Class
"""


class BaseGeometry:
    """
    A class with public methods
    raise exceptions
    """

    def area(self):
        """
        raise an exception that the function
        has not been implemented
        """

        raise Exception("area() can not be implemented")

    def integer_validator(self, name, value):
        """
        valid the instance attribute attribute , value
        else raise an exception
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
