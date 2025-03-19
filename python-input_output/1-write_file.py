#!/usr/bin/python3
"""this module does a lot"""

def write_file(filename="", text=""):
    with open(f"{filename}", "w+") as file:
        return file.write(text)
