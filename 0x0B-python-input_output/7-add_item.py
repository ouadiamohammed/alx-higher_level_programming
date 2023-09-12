#!/usr/bin/python3
"""add_items module"""
import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

mylist = []
file = "add_item.json"

if os.path.exists(file):
    mylist = load_from_json_file(file)

for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i])

save_to_json_file(mylist, file)
