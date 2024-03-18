import unittest
from F import count


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(count([5, 7, 2]), list("x+"))

    def test2(self):
        self.assertEqual(count([4, -5]), list("+"))


if __name__ == '__main__':
    unittest.main()
