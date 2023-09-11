#!/usr/bin/python3
"""this class MyList inherits from list"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """prints a sorted list"""

        print(sorted(self))
