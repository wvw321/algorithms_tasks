x1=int(input())
x2=int(input())
x3=int(input())

if x1 == 0 or x2 == 0 or x3 == 0:
        print("NO")
elif x1 + x2 <= x3:
        print("NO")
elif x2 + x3 <= x1:
        print("NO")
elif x3 + x1 <= x2:
        print("NO")
else:
        print("YES")