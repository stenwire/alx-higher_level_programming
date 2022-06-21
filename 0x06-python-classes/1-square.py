#!/usr/bin/python3
"""Definition of a square class"""


class Square:
    """A class that defines a private instance attribute

    Attributes:
        __size (int): A private instance attribute
    """
    def __init__(self, size):
        """Initialise the size of the square

        Args:
            size (int): represents the size of a square.

        Returns: None
        """
        self.__size = size
