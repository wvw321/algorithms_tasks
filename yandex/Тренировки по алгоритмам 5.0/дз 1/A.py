# p, v = map(int, input().split())
# q, m = map(int, input().split())
# print(len(set(list(range(p - v, p + v + 1)) + list(range(q - m, q + m + 1)))))

p = 0
v = 7
q = 12
m = 5


def count(p, v, q, m):
    x1 = p - v
    x2 = p + v
    y1 = q - m
    y2 = q + m

    def s():
        if y2 < x1:
            return (len(range(x1, x2)) + 1) + (len(range(y1, y2)) + 1)
        if y2 >= x1:
            if y1 <= x1:
                return len(range(y1, x2)) + 1
            else:
                return len(range(x1, x2)) + 1

    # k1 = (x1, x2)
    # k2 = (y1, y2)
    # k1>k2
    if x2 > y2:
        return s()
    # k1<k2
    elif x2 < y2:
        x1, x2, y1, y2 = y1, y2, x1, x2,
        return s()
    # k1=k2
    else:
        return s()


print(count(p, v, q, m))
