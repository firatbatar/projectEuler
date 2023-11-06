import time
from math import sqrt


def integer_sides_for_perimeter(perimeter):
    side_max = perimeter // 2
    sides = list()
    for a in range(1, side_max):
        for b in range(1, side_max):
            c = sqrt(a**2 + b**2)
            if a+b+c == perimeter:
                sides.append((a, b, c))
    return len(sides)/2


start = time.time()

sols = list()
for p in range(0, 1001):
    sols.append(integer_sides_for_perimeter(p))

answer = sols.index(max(sols))
print("Answer: " + str(answer))


print("Time: {:.2f}".format(time.time() - start))
