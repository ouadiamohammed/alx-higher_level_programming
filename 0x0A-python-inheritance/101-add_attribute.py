#!/usr/bin/python3
"""function adds attributs"""


def add_attribute(obj, att, value):
    """adds attributes to objects"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
