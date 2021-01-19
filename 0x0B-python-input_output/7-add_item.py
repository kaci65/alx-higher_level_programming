#!/usr/bin/python3
"""script that adds all arguments to a Python list, and
then save them to a file
"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
with open(filename, encoding="UTF-8", mode="a") as fd:
    try:
        my_list = load_from_json_file(filename)
    except:
        my_list = []

    for i in range(1, len(argv)):
        my_list.append(argv[i])
    save_to_json_file(my_list, filename)
