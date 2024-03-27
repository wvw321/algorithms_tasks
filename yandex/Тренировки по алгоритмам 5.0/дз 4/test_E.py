import unittest
from E import count


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(count(1), (1, 1))

    def test2(self):
        self.assertEqual(count(6), (3, 1))

    def test3(self):
        self.assertEqual(count(2), (2, 1))

    def test21(self):
        self.assertEqual(count(1000000000000000000), (179470704, 1234742859))

    def test0(self):
        self.assertEqual(count(234234),(37,648))
