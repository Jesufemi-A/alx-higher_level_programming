#!/usr/bin/python3
"""
contain function that append file
"""


def append_write(filename="", text=""):
    """
    append text to file
    """

    with open(filename, 'a', encoding='utf-8') as file_a:
        file_added = file_a.write(text)
        return file_added
