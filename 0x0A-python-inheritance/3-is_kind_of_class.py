#!/usr/bin/python3
"""Modul with function that returns true if object is an instance"""


def is_kind_of_class(obj, a_class):
    """function that returns true if object is an instance"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
