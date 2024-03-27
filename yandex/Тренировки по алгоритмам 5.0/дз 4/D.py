def writer(w, arr):
    count = 0
    st = 0
    for x in arr:
        if st + x <= w:
            st += x + 1
        else:
            count += 1
            st = x
    return count


def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def check(m, checkparams):
    first, second = checkparams
    return writer(m, first) == writer(m, second)


def count(first, second, w):
    max_first = max(first)
    max_second = max(second)
    L = lbinsearch(max_first, w - max_second, check, (first, second))
    return L


if __name__ == '__main__':
    w, n, m = map(int, input().split())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    print(count(first, second, w))

    # p = [i for i in range(n)]
    #
    # ans = 0
    # for _ in p:
    #     ok = True
    #     for e in zip(first, second):
    #         if p[e[0]] > p[e[1]]:
    #             ok = False
    #             break
    #         if ok:
    #             ans += 1
    # print(ans)

    # do
    # {
    #     bool
    # ok = true;
    # for (const auto & e: el) {
    # if (p[e.first] > p[e.second]) {
    # ok = false;
    # break;
    # }
    # }
    # if (ok) {
    # ++answer;
    # }
    # }
    # while (next_permutation(begin(p), end(p)));
