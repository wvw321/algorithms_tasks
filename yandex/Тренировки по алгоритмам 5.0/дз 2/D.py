N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

x_con = (0, 1, 1, 0)
y_con = (- 1, 0, 0, 1)

p = 0
for x, y in arr:
    dot = 4
    for xc, yc in zip(x_con, y_con):
        if (xc + x, yc + y) in arr:
            dot -= 1
    p += dot
print(p)
