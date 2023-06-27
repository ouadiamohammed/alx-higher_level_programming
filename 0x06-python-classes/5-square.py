#!/usr/bin/python3
"""defines a square by: (based on 4-square.py)"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """initializes the data"""

        self.size = size

    @property
    def size(self):
        """retrieves size"""

        return self.size

    @size.setter
    def size(self, value):
        """sets size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """ returns the current square area"""

        return (self.__size * self.__size)

    def my_print(self):
        """that prints in stdout the square with the character #"""

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
