#!/usr/bin/python3
"""creating a python object from a json file"""
import json


def load_from_json_file(filename):
    """creates a python object from a json file"""

    with open(filename) as file:
        return json.load(file)
