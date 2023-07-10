#!/usr/bin/python3
"""
Module contains a function that checks for
instance
"""


def inherits_from(obj, a_class):
    """
    return true if the object is an
    instance of a class inherited a_class
    """

    if type(obj) == a_class:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
