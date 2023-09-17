#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """new square initialisation"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for width"""
        return self.__width

    @size.setter
    def size(self, value):
        """sizevalue validation"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updating the values of the rectangle"""

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        """returns the string representation of a the square"""

        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.__x, self.__y,
                                             self.__width)

    def to_dictionary(self):
        """returns the dictionary representation of the square"""

        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
