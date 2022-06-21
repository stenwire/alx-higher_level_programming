#!/usr/bin/python3
"""A square class is defined"""


class Square:
    """A square class that defines a private instance attribute
    
    Attributes:
        __size (int): A private instance attribute
    """
    def __init__(self, size=0):
        """Initialise the size of the square
        
        Args:
            __size (int): represents the size of a square

        Returns:
            None
        """
        type_err = 'size must be an integer'
        val_err = 'size must be >= 0'

        if type(size) != type(10):
            raise TypeError(type_err)
        elif size < 0:
            raise ValueError(val_err)
        else:
            self.__size = size
