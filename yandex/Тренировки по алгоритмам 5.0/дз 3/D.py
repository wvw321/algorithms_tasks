def rezult(n, k, A):
    count = 0
    s = set()
    for i in range(n):
        if count <= k:
            if A[i] in s:
                return "YES"
            else:
                count += 1
                s.add(A[i])
        else:
            s.remove(A[i - k - 1])
            if A[i] in s:
                return "YES"
            else:
                s.add(A[i])

    return "NO"


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print(rezult(n, k, A))
