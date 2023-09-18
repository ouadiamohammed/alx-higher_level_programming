#!/usr/bin/python3
"""class rectangle tests"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestCasesRectangle(unittest.TestCase):
    """tests fro class rectangle"""

    def setUp(self):
        """id reset"""
        Base._Base__nb_objects = 0

    def rectangle_tests(self):
        """tests"""
        rec1 = Rectangle(1, 2)
        self.assertEqual(rec1.id, 4)

        rec2 = Rectangle(10, 2)
        self.assertEqual(rec2.id, 4)

        rec3 = Rectangle(1, 5)
        self.assertEqual(rec3.id, 8)

        rec4 = Rectangle(1, 2, 10)
        self.assertEqual(rec4.id, 4)

        rec5 = Rectangle(1, 2, 6, 6)
        self.assertEqual(rec5.id, 9)

        with self.assertRaises(TypeError):
            Rectangle(-4, 2)
        with self.assertRaises(TypeError):
            Rectangle(4, -2)
        with self.assertRaises(TypeError):
            Rectangle(0, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 2, -6)
        with self.assertRaises(TypeError):
            Rectangle(4, 2, 6, -6)
        with self.assertRaises(TypeError):
            Rectangle("4", 2)
        with self.assertRaises(TypeError):
            Rectangle(2, "4")
        with self.assertRaises(TypeError):
            Rectangle(4, 2, "6")
        with self.assertRaises(TypeError):
            Rectangle(4, 2, 6, "6")


if __name__ == '__main__':
    unittest.main()
