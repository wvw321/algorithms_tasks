# G11, G21 = map(int, input().split(":"))
# G12, G22 = map(int, input().split(":"))
# T = int(input())

def count(G11, G21, G12, G22, T):
    G1 = G11 + G12
    G2 = G22 + G21

    if G1 == G2:
        if T == 1:
            if G12 > G21:
                return 0
            else:
                return 1
        if T == 2:
            if G11 > G22:
                return 0
            else:
                return 1

    if G1 > G2:
        return 0

    if G2 > G1:
        if T == 1:
            if G2 - G1 > G21:
                return G2 - G1
            if G2 - G1 == G21 or G2 - G1 < G21:
                if G2 - G1 + G12 <= G21:
                    return G2 - G1 + 1
                else:
                    return G2 - G1

        if T == 2:
            if G11 > G22:
                return G2 - G1
            else:
                return G2 - G1 + 1
