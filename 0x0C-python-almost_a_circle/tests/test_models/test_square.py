#!/usr/bin/python3
"""square tests"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestCasesSquare(unittest.TestCase):
    """square tests class"""

    def setUp(self):
        """id reset"""
        Base._Base__nb_objects = 0


if __name__ == '__main__':
    unittest.main()
