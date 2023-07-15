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
        Base._Base__nb_object = 0

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
        

if __name__ == '__main__':
    unittest.main()
