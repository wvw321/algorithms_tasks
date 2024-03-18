def count(n, N):
    sum_N = sum(N)
    max_N = max(N)

    if sum_N - max_N >= max_N:
        return sum_N
    else:
        return max_N-(sum_N - max_N)


if __name__ == "__main__":
    n = int(input())
    N = tuple(map(int, input().split()))
    print(count(n, N))
