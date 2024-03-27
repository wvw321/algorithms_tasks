_ = input()
A = set(list(map(int, input().split())))
_ = input()
B = set(list(map(int, input().split())))
_ = input()
C = set(list(map(int, input().split())))

AB = A & B
AC = A & C
BC = B & C

result = AB | AC | BC
result= sorted(result)
for x in result:
    print(x, end=" ")
