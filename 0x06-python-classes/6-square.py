#!/usr/bin/python3
"""defines a square by: (based on 5-square.py)"""


class Square:
    """square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the data"""

        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()


    @property
    def size(self):
        """retrieves size"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get the position of the square"""

        return self._position

    @position.setter
    def position(self, value):
        """set the position of the square"""

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 integers")
        if len([i for i in vale])