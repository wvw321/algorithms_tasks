from collections import Counter
A = Counter(list(input()))
B = Counter(list(input()))

if A == B:
    print('YES')
else:
    print('NO')
