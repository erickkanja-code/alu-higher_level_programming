#!/usr/bin/python3

"""What do you mean i can't afford"""

class BaseGeometry:
    """This is an empty class"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
