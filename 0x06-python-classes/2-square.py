#!/usr/bin/python3
"""defines a square bassed on 1-square.py"""


class Square:
    """Square"""

    def __init__(self, size):
        """Initialize the data"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
