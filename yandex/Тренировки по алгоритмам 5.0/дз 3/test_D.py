import unittest
from D import rezult
import os


def read_data(file):
    with open(os.path.abspath(file), 'r') as f:
        n, k = list(map(int, f.readline().split()))
        A = list(map(int, f.readline().split()))

    return n, k, A


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(rezult(4, 2, [1, 2, 3, 1]), "NO")

    def test2(self):
        self.assertEqual(rezult(4, 1, [1, 0, 1, 1]), "YES")

    def test3(self):
        self.assertEqual(rezult(6, 2, [1, 2, 3, 1, 2, 3]), "NO")

    def test16(self):
        self.assertEqual(rezult(*read_data("data_D/16")), "NO")

    def test17(self):
        self.assertEqual(rezult(*read_data("data_D/17")), "YES")
