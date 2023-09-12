#!/usr/bin/python3
"""read_file function """


def read_file(filename=""):
    """reads the content of a file and print it line by line"""

    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
