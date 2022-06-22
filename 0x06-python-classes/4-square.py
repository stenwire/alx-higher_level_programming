#!/usr/bin/python3
"""creating a square class"""


class Square:
    """A square class that defines a private instance attribute

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retrieve the value of size
        
        Returns:
            The value the square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """"Assigns the value of size to value"""

        self.__size = value

    def area(self):
        """calculate the area of a square
    
        Returns:
            The area of the square
        """
        if type(self.__size) != type(10):
            raise TypeError("size must be an integer")
        else:
            if self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                return self.__size ** 2
