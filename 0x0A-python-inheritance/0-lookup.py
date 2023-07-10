#!/usr/bin/python3
"""
Module contains function that
the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    return list of available attributes and method
    of an object
    """

    return dir(obj)
