#!/usr/bin/python3
"""
contains a function that returns
jsn representation of string
"""


def to_json_string(my_obj):
    """
    returns the json representation of
    an object
    """

    json_rep = json.dumps(my_obj)
    return json_rep
