# n, k, d = map(int, input().split())
import sys
sys.set_int_max_str_digits(0)


def count(n, k, d):
    for x in range(d):
        for i in range(10):
            if (n * 10 + i) % k == 0:
                if i == 0:
                    n = n * 10 ** (d - (x + 1) + 1)
                    return n
                n = n * 10 + i

                break
            else:
                if i == 9:
                    return -1
    return n

# print(count(n, k, d))
