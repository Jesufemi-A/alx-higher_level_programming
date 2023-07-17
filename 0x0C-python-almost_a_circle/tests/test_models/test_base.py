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
        test if id is assigned a value if argument is not None,
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

    def test_id_for_multiple_instances(self):
        """
        test id value for multiple instances
        when id argument is an int
        """
        base1 = Base(1)
        base2 = Base(2)
        base3 = Base(1)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 1)

    def test_id_one_of_instanceIdArgument_None(self):
        """
        test id value for multiple instances when one or two of
        id argument is None
        """
        base1 = Base(1)
        base2 = Base(4)
        base3 = Base()
        base4 = Base(3)
        base5 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 4)
        self.assertEqual(base3.id, 1)
        self.assertEqual(base4.id, 3)
        self.assertEqual(base5.id, 2)

if __name__ == '__main__':
    unittest.main()
