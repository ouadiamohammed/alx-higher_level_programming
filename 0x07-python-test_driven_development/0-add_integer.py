#!usr/bin/python3
"""function that adds two integers"""

def add_integer(a, b=98):
    """function that adds two integers"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be and integer")

    a = int(a)
    b = int(b)
    return a + b
