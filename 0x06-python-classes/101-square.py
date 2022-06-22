#!/usr/bin/python3
"""
This script/module is a demonstration of
use of classes.

Its function is to print in stdout a square with the character #
"""


class Square:
    """"A class representaion of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """"Initialises the Square class

        Args:
            size (int) - represents the size of a square
            position (tuple) -  position of individual square chars

        Returns:
            None
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Defines a square size
        Returns:
            the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Getter function to get the position to value

        Args:
            value (tuple): position of individual square chars

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):
        """Setter function to assign position to value

        Args:
        value (tuple): position of individual square chars

        Returns:
            None
        """
        if type(value) is tuple and len(value) == 2 \
            and value[0] > 0 and value[1] > 0 :
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integer')

    def area(self):
        
        return self.__size ** 2

    def my_print(self):
        """Prints a square with chars

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" "*self.__position[0], end="")
            print('#'*self.__size)

    def __str__(self):
        """String representation of a Square instance

        Returns:
            Formatted string representing the square
        """
        if self.size == 0:
            return ""
        my_str = "\n" * self.position[1] + \
            (" " * self.position[0] + "#" * self.size + "\n") \
            * self.size
        return my_str[:-1]
