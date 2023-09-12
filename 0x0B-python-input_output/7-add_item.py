#!/usr/bin/python3
"""add_items module"""
import json
import sys

save_tp_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list = []

try:
    filename = "add_item.json"
    list = load_from_json_file(filename)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    pass
finally:
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        list.append(arg)
    save_tp_json_file(list, filename)
