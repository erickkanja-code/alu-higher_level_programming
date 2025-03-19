#!/usr/bin/python3
"""Smiling until the end completely"""
import json
def load_from_json_file(filename):
    with open(filename, "r+") as file:
        content = file.read()
        json.loads(content)
