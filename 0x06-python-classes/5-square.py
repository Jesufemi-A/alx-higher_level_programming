#!/usr/bin/python3
"""
This is a module that define a class Square
has validationfor parameter size of class Square
size: size of the square

uses the getter and setter method
"""


class Square:
    """
    This is a class Square
    define the size of a square and has type and value validatio
    """

    def __init__(self, size=0):
        """
        A special method that initilize paramter size
        checks for validation too
        """

        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        """
        returns the size of square using getter method
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        check for validation
        use setter method to access and modify the value
        """

        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must >= 0')
        else:
            self.__size = value

    def area(self):
        """
        This method returns th area of a square
        """

        return self.__size * self.__size

    def my_print(self):
        """
        This  method prints the square in form of # character
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
