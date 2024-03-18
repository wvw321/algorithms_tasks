# n = int(input())
# a = list(map(int,input().split()))


def count(a: list):
    trigger = False
    answer = []
    for i in range(0, len(a) - 1):
        if trigger:
            if a[i + 1] % 2 != 0:
                answer.append("x")

            else:
                answer.append("+")

        else:
            if a[i] % 2 != 0:
                trigger = True
                if a[i + 1] % 2 != 0:
                    answer.append("x")

                else:
                    answer.append("+")
            else:
                answer.append("+")

    return answer


def count(a: list):
    trigger = False
    answer = []
    for i in range(0, len(a) - 1):
        if trigger:
            if a[i + 1] % 2 != 0:
                print("x", end="")
            else:
                print("+", end="")
        else:
            if a[i] % 2 != 0:
                trigger = True
                if a[i + 1] % 2 != 0:
                    print("x", end="")
                else:
                    print("+", end="")
            else:
                print("+", end="")
    return answer
