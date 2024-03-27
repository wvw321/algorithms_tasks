def f(n):
    return n * (n + 1) // 2


def check_(m, n):
    return f(m) < n


def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            l = m + 1
        else:
            r = m
    return l


def count(n):
    L = 1
    r = 2000000000
    l = lbinsearch(L, r, check_, n)

    sum = l + 1
    if l % 2 == 1:
        p = f(l - 1)
        num = n - p
        den = sum - num
    else:
        p = f(l - 1)
        den = n - p
        num = sum - den
    return int(num), int(den)


if __name__ == "__main__":
    n = int(input())
    num, den = count(n)
    print(str(num) + "/" + str(den))
