#!/usr/bin/python3
"""
A function that print a string
"""


def say_my_name(first_name, last_name=""):
    """
    This function  prints a string and uses placeholder  to inser names
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif first_name == " ":
        print("My name is {} {}".format(first_name, last_name))
    elif isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {} {}".format(first_name, last_name))
