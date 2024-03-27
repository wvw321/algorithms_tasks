def k_sum_k(k):
    return ((k * (k + 1) // 2) * k) - ((k - 1) * k * (k + 1)) // 3


def k_sum_z(k):
    return (k * (k + 1)) // 2 - 1


def k_sum(k):
    return k_sum_k(k) + k_sum_z(k)


def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l


def check_(i, n):
    return k_sum(i) <= n


def count(n):
    return rbinsearch(1, 10 ** 9, check_, n)


if __name__ == "__main__":
    n = int(input())
    if n == 0:
        print(0)
    else:
        print(count(n))
