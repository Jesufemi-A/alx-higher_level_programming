#!/usr/bin/python3
"""
contain function that write string to file
"""


def write_file(filename="", text=""):
    """
    write string to file and return the
    number character written
    """

    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written
