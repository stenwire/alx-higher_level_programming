#!/usr/bin/python3
"""
This module contains the "Base" class
"""

class Base:
    """A base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize the base class"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects+=1
            self.id = Base.__nb_objects
