from collections import Counter


def count(size, A):
    if size == 1:
        return 0

    A = Counter(A)
    sorted_A = sorted(A.items(), key=lambda item: item[0])

    if len(sorted_A) == 1:
        return 0


    max_duo = 0
    max_solo = 0
    for i in range(1, len(sorted_A)):
        max_solo = max(max_solo, sorted_A[i - 1][1], sorted_A[i][1])
        if abs(sorted_A[i - 1][0] - sorted_A[i][0]) == 1:
            max_duo = max(max_duo, (sorted_A[i - 1][1] + sorted_A[i][1]))

    if max_duo == 0:
        return size - max_solo
    else:
        return size - max_duo


if __name__ == "__main__":
    size = int(input())
    A = list(map(int, input().split()))
    print(count(size, A))
