#!/usr/bin/python3
""" class Rectangle that defines a rectangle"""


class Rectangle:
    """defines a rectangle by: (based on 1-rectangle.py)"""

    def __init__(self, width=0, height=0):
        """initializes a rectangle with width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """set width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """set width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """set height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """set height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns string representation of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""

        printable = ""
        for i in range(self.__height):
            for j in range(self.__width):
                printable += "#"
            if i < self.__height - 1:
                printable += "\n"
        return (printable)

    def __repr__(self):
        """returns str representation of Rectangle"""

        return "Rectangle({}, {})".format(self.__width,  self.__height)
