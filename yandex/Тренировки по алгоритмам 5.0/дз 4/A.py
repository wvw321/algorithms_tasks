def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l


def check_L(i, checkparams):
    arr, L = checkparams
    return arr[i] >= L


def check_R(i, checkparams):
    arr, L = checkparams
    return arr[i] <= L


def count(n_size, N, q):
    N.sort()
    ans = []
    L_n = N[0]
    R_n = N[-1]

    for l, r in q:
        if r < L_n or R_n < l:
            ans.append(0)
            continue
        L = lbinsearch(0, n_size - 1, check_L, (N, l))
        R = rbinsearch(0, n_size - 1, check_R, (N, r))
        ans.append(R - L + 1)
    return ans


if __name__ == "__main__":
    n_size = int(input())
    N = list(map(int, input().split()))
    k = int(input())
    q = [list(map(int, input().split())) for _ in range(k)]

    for x in count(n_size, N, q):
        print(x, end=" ")


