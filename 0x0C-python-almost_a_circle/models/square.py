#!/usr/bin/python3
"""
Contains the "Square" class
"""

from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        j = len(args)
        if j:
            self.id = args[0]
            if j > 1:
                self.size = args[1]
            if j > 2:
                self.x = args[2]
            if j > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Rectangle instance to dictionary representation"""
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.size
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
    
    def __str__(self):
        """String represenation of class"""
        s1 = '('+str(self.id)+')'
        s2 = str(self.x)+"/"+str(self.y)
        s3 = str(self.height)
        return '[Square]' + ' ' + s1 + ' ' + s2 + ' ' + '-' + ' ' + s3
