#!/usr/bin/python3
"""test_base module"""
import unittest
from models.base import Base


class BaseTests(unittest.TestCase):
    """class BaseTests"""

    def tests(self):
        """tests"""
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base3 = Base()
        self.assertEqual(base3.id, 3)

        base4 = Base()
        self.assertEqual(base4.id, 4)

        base10 = Base()
        self.assertEqual(base10.id, 10)

        if __name__ == '__main__':
            unittest.main()
