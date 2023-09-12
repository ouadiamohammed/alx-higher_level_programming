#!/usr/bin/python3
"""write_file function """


def write_file(filename="", text=""):
    """writes string to a file and returns number of chars written"""

    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(text))
