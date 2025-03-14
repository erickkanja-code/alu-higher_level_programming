#!/usr/bin/python3


"""There needs to be more labels on this"""



class Square:
    """This class uses exceptions to validate the size."""

    def __init__(self, size=0):
        self.size = size  # Using the setter to validate the size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # Correctly check the type of 'value'
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def perimeter(self):
        return 4 * self.__size  # Perimeter = 4 * size
    def my_print(self):
        for i in range(self.__size):
            if self.__size > 0:
                print('#' * self.__size)
            else:
                print()
