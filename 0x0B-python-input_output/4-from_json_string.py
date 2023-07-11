#!/usr/bin/python3
"""
contains from_json_string()
"""
import json


def from_json_string(my_str):
    """
    returns an object represented by json string
    """

    obj_rep = json.loads(my_str)
    return obj_rep
