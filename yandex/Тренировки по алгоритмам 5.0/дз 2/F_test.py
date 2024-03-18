import unittest
from F import count

arr26 = list(map(int, "299 11 829 583 357 873 384 283 251 828 703 672 376 975 "
                      "99 734 78 413 884 776 962 45 776 208 501 643 207 37 446 "
                      "180 850 510 883 925 35 718 927 296 536 452 485 52 650 205"
                      " 890 127 490 936 993 299 466 190 280 3 633 556 431 769 800 "
                      "431 537".split()))


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(count(5, [1, 2, 3, 4, 5], 3, 5, 2), 5)

    def test2(self):
        self.assertEqual(count(5, [1, 2, 3, 4, 5], 15, 15, 2), 4)

    def test3(self):
        self.assertEqual(count(5, [5, 4, 3, 2, 1], 2, 5, 2), 5)

    def test5(self):
        self.assertEqual(count(9, [707, 805, 279 ,713, 584 ,352, 923 ,1000, 237], 29, 38, 1), 1000)

    def test6(self):
        self.assertEqual(count(9, [89  , 527, 177, 573, 258, 201], 25, 28, 708), 89)
    def test26(self):
        self.assertEqual(count(61, arr26, 96688499, 401051285, 6763618), 993)


if __name__ == '__main__':
    unittest.main()
