#!/usr/bin/python3
"""An empty rectangle class"""

class Rectangle():
    """Fun-fact: A rectangle in geometry,is a plane figure with three sides"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @width.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        rect_area = self.__width * self.__height
        return rect_area

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            rect_peri = 0
            return rect_peri
        else:
            rect_peri = 2 * (self.__width + self.__height)
            return rect_peri

    def __str__(self):
        """returns string representation of the rectangle"""
        my_str = ''
        if self.__width != 0 and self.__height != 0:
            i = 0
            while i < self.__height:
                i+=1
                my_str += '#'*self.__width  + '\n'
            return my_str
        else:
            return my_str
