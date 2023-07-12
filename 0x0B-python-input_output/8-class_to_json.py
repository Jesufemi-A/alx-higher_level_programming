#!/usr/bin/python3
"""
class to json module
"""


def class_to_json(obj):
    """
    class to json
    """

    dict_desc = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            dict_desc[key] = value
    return dict_desc
