import unittest
from B import count


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(count(7), 2)
    def test2(self):
        self.assertEqual(count(1), 1)

    def test5(self):
        self.assertEqual(count(5), 1)

    def test8(self):
        self.assertEqual(count(14), 2)

    def test42(self):
        self.assertEqual(count(117055765888857794),  888887)