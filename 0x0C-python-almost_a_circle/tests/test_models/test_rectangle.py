#!/usr/bin/python3
"""
test for class Rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO

class TestRectangle(unittest.TestCase):
    """
    define test for Rectangle
    """

    def setUp(self):
        """
        execute before each test
        """
        Base._Base__nb_objects = 0
        
    def test_attribute_value(self):
        """
        test if the argument are properly assigned
        """
        rect = Rectangle(2, 3, 2, 3, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_multiple_instantiation(self):
        """
        test if arguments are properly assigned to attribute
        with multiple instantiation
        """
        rect = Rectangle(2, 3, 2, 3, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        
        rect1 = Rectangle(3, 5, 1, 2, 2)
        self.assertEqual(rect1.id, 2)
        self.assertEqual(rect1.width, 3)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 1)
        self.assertEqual(rect1.y, 2)

    def test_id_is_assigned_int_after_multiple_None_argument(self):
        """
        test that __nb_obects is increment and assigned to id, after
        mutiple instantiation with argument None for id
        """
        rect = Rectangle(2, 3, 2, 3)
        self.assertEqual(rect.id, 1)

        rect1 = Rectangle(3, 5, 1, 2)
        self.assertEqual(rect1.id, 2)

    def test_width_and_height_greater_zero(self):
        """
        test Value error is raised if  argument <= 0
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 0, 1, 1)
            if width <= 0:
                raise ValueError('width must be > 0')
            if height <= 0:
                raise ValueError('height must be > 0')
    
    def test_x_y_not_less_xer0(self):
        """
        test that x and y are >= 0
        """
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 1, -1, -1)
            if x < 0:
                raise ValueError('x must be >= 0')
            if y < 0:
                raise ValueError('y must be >= 0')

    def test_input_is_an_integer(self):
        """
        test that input are type int
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(1.22, 2.22, 3.22, 4.22)
            if type(width) != int:
                raise TypeError('width must be an integer')
            if type(height) != int:
                raise TypeError('height must be integer')
            if type(x) != int:
                raise TypeError('x must be intger')
            if type(y) != int:
                raise TypeError('y must be integer')
    
    def test_display_displays(self):
        """
        test that display method works properly
        """
        rect = Rectangle(2, 5)
        with patch('sys.stdout', new_callable = StringIO()) as out:
            rect.display()
            self.assertEqual(out.getvalue(), "##\n##\n##\n##\n##\n")
    
    def test_args_value_assigned_to_attributes(self):
        """
        test that the *args values are properly assigned to the attributes
        """
        args = (2, 3, 4, 2, 3)
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(*args)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
