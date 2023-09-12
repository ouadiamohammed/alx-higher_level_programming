#!/usr/bin/python3
"""returns the Python object representation of a jason string"""
import json


def from_json_string(my_str):
    """returns the Python object representation of a jason string"""

    return json.loads(my_str)
