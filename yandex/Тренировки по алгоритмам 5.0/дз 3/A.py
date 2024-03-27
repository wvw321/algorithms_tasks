n = int(input())

for i in range(n):
    if i == 0:
        k = int(input())
        s = set(input().split())
    else:
        k = int(input())
        s0 = set(input().split())
        s = s0 & s

print(len(s))
s=sorted(s)
for x in s:
    print(x, end=' ')
