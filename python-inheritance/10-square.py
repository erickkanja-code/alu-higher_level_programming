#!/usr/bin/python3

"""What do you mean i can't afford"""

class BaseGeometry:
    """This is an empty class"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """range autobiography is what we saying"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    """this is a very scary and dirty class"""
    def __init__(self, width, height):
        """driving from isinya to kiren"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """this is quite relevant so"""
        return self.__width * self.__height
    def __str__(self):
        """out and about """
        return f"[Rectangle] {self.__width/self.__height}"

class Square(Rectangle):
    """A lot of doing sth about it"""
    def __init__(self, size):
        """5 days a week sth is happening"""
        self.integer_validator("size", size)
    
        super().__init__(size, size)
        self.__size = size
    def area(self):
        """now its a lifestyle thing"""
        return self.__size * self.__size

    def __str__(self):
        """job at ghetto radio"""
        return f"[Square] {self.__size}/{self.__size}"

