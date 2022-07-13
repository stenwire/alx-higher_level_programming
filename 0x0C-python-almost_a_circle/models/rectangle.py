#!/usr/bin/python3
"""
Contains the "Rectangle" class
"""

from models.base import Base


class Rectangle(Base):
    """A representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        
        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter for height"""
        # self.__height = value
        if type(value) is not int:
            raise TypeError('height must be an integer')
        
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        # self.__x = value
        if type(value) is not int:
            raise TypeError('x must be an integer')
        
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        """getter for x"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        # self.__y = value
        if type(value) is not int:
            raise TypeError('y must be an integer')
        
        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """print a display of the rectangle"""
        i = self.__width
        k = self.__x
        m = self.__y
        if m > 0:
            print('\n'*m)
        for j in range(self.__height):
            if i == self.__width:
                print(' '*k + '#'*i)


    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        j = len(args)
        # print(j)
        if j:
            self.id = args[0]
            if j > 1:
                self.width = args[1]
            if j > 2:
                self.height = args[2]
            if j > 3:
                self.x = args[3]
            if j > 4:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Rectangle instance to dictionary representation"""
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['width'] = self.width
        my_dict['height'] = self.height
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
    
    def __str__(self):
        """informal string representation of the rectangle"""
        s1 = '('+str(self.id)+')'
        s2 = str(self.__x)+"/"+str(self.__y)
        s3 = str(self.__width)+'/'+str(self.__height)
        return '[Rectangle]' + ' ' + s1 + ' ' + s2 + ' ' + '-' + ' ' + s3
