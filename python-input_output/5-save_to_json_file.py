#!/usr/bin/python3
import json
"""she is Ugandan Kikuyu"""

def save_to_json_file(my_obj, filename):
    """This is quite silly what does this have"""
    with open(filename, "w+") as file:
        my_obj_json = json.dumps(my_obj)
        file.write(my_obj_json)
