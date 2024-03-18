import unittest
from E import count
from E_test_nunms import test12_num


class TestStringMethods(unittest.TestCase):

    def testKR1(self):
        self.assertEqual(count(21, 108, 1, ), 216)

    def testKR2(self):
        self.assertEqual(count(5, 12, 4, ), -1)

    def test12(self):
        self.assertEqual(count(29420920, 98069736, 69929), test12_num)


if __name__ == '__main__':
    unittest.main()
