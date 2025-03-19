#!/usr/bin/python3
"""this module does a lot"""

def write_file(filename="", text=""):
    """I've sold a piece of equipment"""
    with open(f"{filename}", "w+") as file:
        return file.write(text)
