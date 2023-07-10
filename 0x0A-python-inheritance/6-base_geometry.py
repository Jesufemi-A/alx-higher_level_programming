#!/usr/bin/python3
"""
Contains class BaseGeometry
updating BaseGeometry
"""


class BaseGeometry:
    """
    raise an exception error with the message,
    area is not implented
    """

    def area(self):
        raise Exception('area() is not implemented')
