#!/usr/bin/python3
"""A square class is defined"""


class Square:
    """A square class that defines a private instance attribute

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initialise the size of the square

        Args:
            size (int): represents the size of a square

        Returns:
            None
        """
        type_err = 'size must be an integer'
        val_err = 'size must be >= 0'
        if type(size) is not int:
            raise TypeError(type_err)
        else:
            if size < 0:
                raise ValueError(val_err)
            else:
                self.__size = size

    def area(self):
        """calculate the area of a square
        
        Args:
            None

        Returns:
            The area of the square
        """
        s_area = (self.__size) ** 2
        return s_area
