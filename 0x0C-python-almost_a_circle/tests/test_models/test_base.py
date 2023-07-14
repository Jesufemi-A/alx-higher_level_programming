import unittest
from models.base import Base


class TestBase(unittest.TestCase): 
    
    def test_id(self):
        base1 = Base(1)
        self.assertEqual(base1.id, 1)

