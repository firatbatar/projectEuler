from time import time
from itertools import permutations
start = time()


class Polygonal:
    @staticmethod
    def triangle(n):
        return int(n * (n + 1) / 2)

    @staticmethod
    def square(n):
        return int(n * n)

    @staticmethod
    def pentagonal(n):
        return int(n * (3*n - 1) / 2)

    @staticmethod
    def hexagonal(n):
        return int(n * (2*n - 1))

    @staticmethod
    def heptagonal(n):
        return int(n * (5*n - 3) / 2)

    @staticmethod
    def octagonal(n):
        return int(n * (3*n - 2))


def is_cyclic(num1, num2):
    return str(num1)[2:] == str(num2)[0:2]


def main():
    for p in perms:
        for a in polygonals[p[0]]:
            for b in polygonals[p[1]]:
                if not is_cyclic(a, b):
                    continue
                else:
                    for c in polygonals[p[2]]:
                        if not is_cyclic(b, c):
                            continue
                        else:
                            for d in polygonals[p[3]]:
                                if not is_cyclic(c, d):
                                    continue
                                else:
                                    for e in polygonals[p[4]]:
                                        if not is_cyclic(d, e):
                                            continue
                                        else:
                                            for f in polygonals[p[5]]:
                                                if not is_cyclic(e, f) or not is_cyclic(f, a):
                                                    continue
                                                else:
                                                    return [a, b, c, d, e, f]


triangles = []
squares = []
pentagonals = []
hexagonals = []
heptagonals = []
octagonals = []
polygonals = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]
perms = list(permutations(range(6)))

# generate 4-digits
for i in range(6):
    num = 0
    while True:
        if i == 0:
            tNum = str(Polygonal.triangle(num))
            if len(tNum) == 4:
                triangles.append(tNum)
            elif len(tNum) > 4:
                break
            num += 1
        elif i == 1:
            sNum = str(Polygonal.square(num))
            if len(sNum) == 4:
                squares.append(sNum)
            elif len(sNum) > 4:
                break
            num += 1
        elif i == 2:
            pNum = str(Polygonal.pentagonal(num))
            if len(pNum) == 4:
                pentagonals.append(pNum)
            elif len(pNum) > 4:
                break
            num += 1
        elif i == 3:
            hNum = str(Polygonal.hexagonal(num))
            if len(hNum) == 4:
                hexagonals.append(hNum)
            elif len(hNum) > 4:
                break
            num += 1
        elif i == 4:
            hNum = str(Polygonal.heptagonal(num))
            if len(hNum) == 4:
                heptagonals.append(hNum)
            elif len(hNum) > 4:
                break
            num += 1
        elif i == 5:
            oNum = str(Polygonal.octagonal(num))
            if len(oNum) == 4:
                octagonals.append(oNum)
            elif len(oNum) > 4:
                break
            num += 1

chain = main()
print(chain)
answer = 0
for i in chain:
    answer += int(i)
print(answer)
print(f"Time {time() - start:.3f}")

