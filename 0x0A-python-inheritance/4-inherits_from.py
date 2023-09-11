#!/usr/bin/python3
"""Module with function that returns True if the object is instance """


def inherits_from(obj, a_class):
    """unction that returns True if the object is instance"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
