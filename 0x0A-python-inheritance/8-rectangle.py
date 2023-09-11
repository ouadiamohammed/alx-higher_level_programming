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
