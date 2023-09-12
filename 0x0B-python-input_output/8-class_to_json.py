#!/usr/bin/python3
"""this module defines a python class-to-json function"""


def class_to_json(obj):
    return obj.__dict__
