#!/usr/bin/python3
"""class inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """initializes rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area calculated"""

        return self.__width * self.__height

    def __str__(self):
        """return the print() and str() representation of a rectangle"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
