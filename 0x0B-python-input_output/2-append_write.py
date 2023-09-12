#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """adds string to already existing file"""

    with open(filename, mode="a", encoding="utf-8") as file:
        return (file.write(text))
