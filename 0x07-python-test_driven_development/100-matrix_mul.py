#!/usr/bin/python3
"""
This module multiply 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    multiple two matrices
    must be list of list of float or int type
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list)
