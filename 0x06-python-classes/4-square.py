#!/usr/bin/python3
"""creating a square class"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a square
    """
    def __init__(self, size=0):
        """initializes the square

        Args:
            size (int): size of a square

        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the value of size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Assigns the value of size to value

        Args:
            value (int): the size of a size of the square

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """calculate the area of a square
    
        Returns:
            The area of the square
        """
        return (self.__size) ** 2
