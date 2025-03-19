#!/usr/bin/python3
"""Student to JSON"""
class Student:
    """This is a class called student"""
    def __init__(self, first_name, last_name, age):
        """Just to initialize the names and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This is the last"""
        return self.__dict__
