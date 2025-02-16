poly2 = [3, 2, 2, -3, 1, 1, 0]
x = 2
fx = 0
for y in range(poly2[0]):
    fx += poly2[2 * y + 1] * x **  poly2[2 * (y + 1)]
print("fx:",fx)
