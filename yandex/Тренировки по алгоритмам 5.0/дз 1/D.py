positive = (1, 2, 3, 4, 5, 6, 7, 8)
negative = (-1, -2, -3, -4, -5, -6, -7, -8)
zero = (0, 0, 0, 0, 0, 0, 0, 0)
# B
Bx1 = positive
By1 = positive

Bx2 = negative
By2 = negative

Bx3 = negative
By3 = positive

Bx4 = positive
By4 = negative

Bx = (Bx1, Bx2, Bx3, Bx4)
By = (By1, By2, By3, By4)
# R
Rx1 = zero
Ry1 = positive

Rx2 = zero
Ry2 = negative

Rx3 = positive
Ry3 = zero

Rx4 = negative
Ry4 = zero

Rx = (Rx1, Rx2, Rx3, Rx4)
Ry = (Ry1, Ry2, Ry3, Ry4)

piece = {"R": [],
         "B": []}

for y in range(8):
    data = list(input())
    for x in range(8):
        if data[x] == "R":
            piece["R"].append((x + 1, y + 1))
        if data[x] == "B":
            piece["B"].append((x + 1, y + 1))

all_piece = piece["R"] + piece["B"]


def cell_calculation(XX, YY, piece):
    impact_cells = []
    for X, Y in piece:
        for data in zip(XX, YY):
            for x, y in zip(data[0], data[1]):
                x_cell = X + x
                y_cell = Y + y
                if 9 > x_cell > 0 and 9 > y_cell > 0:
                    if (x_cell, y_cell) not in all_piece:
                        impact_cells.append((x_cell, y_cell))
                    else:
                        break
                else:
                    break
    return impact_cells


if len(piece["R"]) != 0:
    impact_cells_R = cell_calculation(Rx, Ry, piece["R"])
else:
    impact_cells_R = []
if len(piece["B"]) != 0:
    impact_cells_B = cell_calculation(Bx, By, piece["B"])
else:
    impact_cells_B = []

impact_cells = len(set(impact_cells_R + impact_cells_B)) + len(all_piece)

print(64 - impact_cells)


