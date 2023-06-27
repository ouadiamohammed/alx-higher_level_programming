#!/usr/bin/python3
"""defining new class square"""


class Square:
    """square"""

    def __init__(self, size=0):
        """initializes the data"""

        self.size = size

    @property
    def size(self):
        """returns size of square"""
        return self.__size

    def area(self):
        """return the current square area"""

        return (self.__size * self.__size)

    @size.setter
    def size(self, value):
        """sets size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
