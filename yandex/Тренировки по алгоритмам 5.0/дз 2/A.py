import math

K = int(input())
arr = []
xmax = 0
ymax = 0
xmin = math.inf
ymin = math.inf
for _ in range(K):
    x, y = map(int, input().split())
    xmax = max(xmax, x)
    ymax = max(ymax, y)
    xmin = min(xmin, x)
    ymin = min(ymin, y)

print(xmin, ymin, xmax, ymax)
