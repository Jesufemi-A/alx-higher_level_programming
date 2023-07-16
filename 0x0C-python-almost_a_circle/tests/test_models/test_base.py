import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    defining class TestBase
    """

    def setUp(self):
        """
        execute before each test is executed
        """
        Base._Base__nb_objects = 0

    def test_id_equals_None(self):
        """
        test if __nb_object is incremented and assigned to id,
        if argument for id is None
        """
        base_t = Base()
        self.assertEqual(base_t.id, 1)

    def test_id_valid_int(self):
        """
        test if id is assigned a value if arguement is not None,
        but int
        """
        base_t = Base(1)
        self.assertEqual(base_t.id, 1)

    def test_for_more_than_one_argument(self):
        """
        test if user enter more than one argument
        """
        with self.assertRaises(TypeError):
            base_t = Base(1, 2)
            raise TypeError('only one argument should be enter')


if __name__ == '__main__':
    unittest.main()
