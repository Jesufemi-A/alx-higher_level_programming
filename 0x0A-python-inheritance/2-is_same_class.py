#!/usr/bin/python3
"""
Module contains is_same_class function
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of a_class
    else return False

    parameters:
    obj: object of class to be compared
    a_class: class to be compared
    return: True or False
    """

    if type(obj) == a_class:
        return True
    else:
        return False
