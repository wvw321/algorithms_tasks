import unittest
from C import count


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(count(4, [1, 5, 2, 1]), 1)

    def test2(self):
        self.assertEqual(count(4, [5, 12, 4, 3]), 24)

    def test4(self):
        self.assertEqual(count(2, [999, 1000]), 1)

    def test6(self):
        self.assertEqual(count(3, [3, 4, 5]), 12)
