#!/usr/bin/python3

"""This is a conquered all approach"""

class Square:
    """Very fast approach"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    # Getter for size
    @property
    def size(self):
        return self.__size

    # Setter for size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # Getter for position
    @property
    def position(self):
        return self.__position

    # Setter for position
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    # Method to calculate the area
    def area(self):
        return self.__size ** 2

    # Method to print the square
    def my_print(self):
        if self.__size == 0:
            print()  # Print an empty line if size is 0
            return

        # Print spaces based on position[1]
        for _ in range(self.__position[1]):
            print()

        # Print the square using the size and position[0]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

