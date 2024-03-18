import unittest
from B import count


class TestStringMethods(unittest.TestCase):

    def testKR1(self):
        self.assertEqual(count(0, 0, 0, 0, 1), 1)

    def testKR2(self):
        self.assertEqual(count(0, 0, 0, 0, 2), 1)

    def testKR3(self):
        self.assertEqual(count(1, 1, 1, 1, 1), 1)

    def testKR4(self):
        self.assertEqual(count(1, 1, 1, 1, 2), 1)

    def testKR5(self):
        self.assertEqual(count(0, 1, 1, 0, 1), 1)

    def testKR6(self):
        self.assertEqual(count(0, 1, 1, 0, 2), 1)

    def testKR7(self):
        self.assertEqual(count(1, 0, 0, 1, 1), 1)

    def testKR8(self):
        self.assertEqual(count(1, 0, 0, 1, 2), 1)

    def testKR9(self):
        self.assertEqual(count(1, 2, 3, 2, 1), 0)

    def testKR10(self):
        self.assertEqual(count(1, 2, 3, 2, 2), 1)

    def testKM1(self):
        self.assertEqual(count(0, 1, 1, 1, 1), 1)

    def testKM2(self):
        self.assertEqual(count(0, 1, 1, 1, 2), 2)

    def testKM3(self):
        self.assertEqual(count(1, 1, 1, 3, 1), 2)

    def testKM4(self):
        self.assertEqual(count(1, 1, 1, 3, 2), 3)

    def test1(self):
        self.assertEqual(count(0, 2, 0, 3, 1), 5)

    def test2(self):
        self.assertEqual(count(0, 2, 0, 3, 2), 6)

    def test3(self):
        self.assertEqual(count(0, 0, 1, 1, 1), 0)
    def test4(self):
        self.assertEqual(count(0, 0, 1, 1, 2), 1)

    def test4(self):
        self.assertEqual(count(5, 2, 2, 5, 2), 1)

    def test20(self):
        self.assertEqual(count(5, 2, 0, 5, 1), 3)
    def test26(self):
        self.assertEqual(count(1, 4, 4, 2, 1), 1)
    def test29(self):
        self.assertEqual(count(4, 2, 0, 3, 1), 2)

    def test48(self):
        self.assertEqual(count(0, 5, 2, 1, 1), 4)


if __name__ == '__main__':
    unittest.main()
