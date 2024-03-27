import unittest
from C import count
import os


# def read_data(file):
#     with open(os.path.abspath(file), 'r') as f:
#         n, k = list(map(int, f.readline().split()))
#         A = list(map(int, f.readline().split()))
#
#     return n, k, A


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(count(5, [1, 2, 3, 4, 5]), 3)

    def test2(self):
        self.assertEqual(count(10, [1, 1, 2, 3, 5, 5, 2, 2, 1, 5]), 4)

    def test3(self):
        self.assertEqual(count(1, [33292]), 0)

    def test5(self):
        self.assertEqual(count(10, [22238 ,22238, 22238 ,22238 ,22238 ,22238 ,22238, 22238 ,22238 ,22238]), 0)

    def test6(self):
        self.assertEqual(count(10, [22238, 38788, 73611, 22861, 18865, 52721,
                                    85325, 98901, 72035, 74803]), 9)
