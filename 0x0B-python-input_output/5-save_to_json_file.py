#!/usr/bin/python3
"""writes an object to a text file, using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using json representation"""

    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
