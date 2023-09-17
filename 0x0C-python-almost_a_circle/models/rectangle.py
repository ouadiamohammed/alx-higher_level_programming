#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """this class inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle sub class"""

        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")

        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")

        self.__y = value

    def area(self):
        """returns the area of the rectangle"""

        return (self.__height * self.__width)

    def display(self):
        """prints the rectangle with '#' char"""

        rectangle = ""
        symbol = "#"

        print("\n" + self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (symbol * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """returns string representation of the rectangle"""

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

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

    def to_dictionary(self):
        """dictionary representation of the rectangle"""

        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
