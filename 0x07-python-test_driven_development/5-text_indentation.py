#!/usr/bin/python3
"""
contains a function text_indentation
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    elif isinstance(text, str):
        for i, t in enumerate(text):
            if t == ':' or t == '.' or t == '?':
                print(t, end="\n\n")
            else:
                print(t, end="")
