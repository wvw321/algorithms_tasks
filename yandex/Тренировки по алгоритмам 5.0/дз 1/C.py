n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

count = 0
for x in a:
    tab = x // 4
    ost = x % 4
    if ost == 3:
        tab += 2
    if ost == 2:
        tab += 2
    if ost == 1:
        tab += 1
    if ost == 0:
        tab += 0
    count += tab
print(count)