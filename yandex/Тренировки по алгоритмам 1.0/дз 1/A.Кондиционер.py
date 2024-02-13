T = input().split()
Troom = int(T[0])
Tcond = int(T[1])
mod = str(input())

if mod == "auto":
    answer = Tcond
elif mod == "fan":
    answer = Troom
elif mod == "freeze":
    if Troom > Tcond:
        answer = Tcond
    else:
        answer = Troom
else:
    if Troom < Tcond:
        answer = Tcond
    else:
        answer = Troom

print(answer)
