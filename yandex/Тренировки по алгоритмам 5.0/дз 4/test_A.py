import unittest
from A import count
import os


def read_data(file):
    with open(os.path.abspath(file), 'r') as f:
        n_size = int(f.readline())
        N = list(map(int, f.readline().split()))
        k = int(f.readline())
        q = [list(map(int, f.readline().split())) for _ in range(k)]

    return n_size, N, q


def read_data_ans(file):
    with open(os.path.abspath(file), 'r') as f:
        Ans = list(map(int, f.readline().split()))
    return Ans

    return n_size, N, q


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(count(*read_data("data_A/1")),
                         read_data_ans("data_A/1.a"))

    def test2(self):
        self.assertEqual(count(*read_data("data_A/2")),
                         read_data_ans("data_A/2.a"))
