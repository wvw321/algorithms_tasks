import unittest
from A import count


class TestStringMethods(unittest.TestCase):

    def testKR1(self):
        self.assertEqual(count(0, 7, 12, 5), 25)


if __name__ == '__main__':
    unittest.main()
