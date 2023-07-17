#!/user/bin/python3
"""
contains class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        intialises the instance attributes
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter for private attribute __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter  for accessing and setting private attribute __width
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        """
        method that print rectangle and use x as x axis
        y as y axis
        """
        for y_axis in range(self.y):
            print()
        for h in range(self.height):
            if self.x > 0:
                for x_axis in range(self.x):
                    print(' ', end='')
            for w in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        return a string representation
        """
        return f"[Rectangle] ({self.id}) \
                {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        update and assign values to the attributes
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        return a dictionary representation of the class Rectangle
        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
