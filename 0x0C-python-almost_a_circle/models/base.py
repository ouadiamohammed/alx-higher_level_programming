#!/usr/bin/python3
"""defines a base class"""
import json
import csv
import turtle


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """new Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects