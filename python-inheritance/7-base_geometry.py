#!/usr/bin/python3

"""What do you mean i can't afford"""

class BaseGeometry:
    """This is an empty class"""
    def area(self):
        """Lets see how this goes:
        >>> test1 = BaseGeometry()
        >>> test1.area()
        Traceback (most recent call last):
        ...
        Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        >>> test2 = BaseGeometry()
        >>> test2.integer_validator("Erick", "10")
        Traceback (most recent call last):
        ...
        TypeError: Erick must be an integer
        
        >>> test2 = BaseGeometry()
        >>> test2.integer_validator("Erick", 0)
        Traceback (most recent call last):
        ...
        ValueError: Erick must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
