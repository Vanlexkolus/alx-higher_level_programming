#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list, and then
save them to a file
"""


import json
import sys
import os
saver = __import__("5-save_to_json_file").save_to_json_file
loader = __import__("6-load_from_json_file").load_from_json_file


The_list = "add_item.json"

if os.path.exists(The_list):
    My_list = loader(The_list)
else:
    My_list = []
My_list.extend(sys.argv[1:])
saver(My_list, The_list)
