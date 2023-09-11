#!/usr/bin/python3
"""checks if the object is an instance of the class"""


def is_same_class(obj, a_class):
    """checks if the object is an instance of the class"""
    if type(obj) == a_class:
        return True
    else:
        return False
