#!/usr/bin/python3
"""
Module contains is_kind_of_class() function
"""


def is_kind_of_class(obj, a_class):
    """
    return True if obj is an instance of a class that inherited from
    a_class
    else return False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
