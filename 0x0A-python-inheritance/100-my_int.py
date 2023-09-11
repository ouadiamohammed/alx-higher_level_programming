#!/usr/bin/python3
"""claas MyInt"""


class MyInt(int):
    """this class inherits from int and reverses behaviour of != and =="""

    def __eq__(self, other):
        """inverts == to !="""

        return super().__ne__(other)

    def __ne__(self, other):
        """inverts != to =="""

        return super().__eq__(other)
