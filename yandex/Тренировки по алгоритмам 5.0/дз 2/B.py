N, K = map(int, input().split())
arr = tuple(map(int, input().split()))
index = tuple(range(1, K + 1))

max_all = 0
for i in range(N):
    indexes = tuple(map(lambda x: x + i, index))
    max_local = 0
    for ind in indexes:
        if ind < N:
            delta = arr[ind] - arr[i]
            max_local = max(max_local, arr[ind] - arr[i])
            delta
    max_all = max(max_all, max_local)
print(max_all)
