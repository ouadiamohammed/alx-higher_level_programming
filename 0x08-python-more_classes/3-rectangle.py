#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """a class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the width and height of a rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """self width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """set height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """set new height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value


    def area(self):
        """returns the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns a string representation of a rectangle"""

        if self._width == 0 or self.__height == 0:
            return ""

        return "\n".join(["#" * self.__width] * self.__height)
