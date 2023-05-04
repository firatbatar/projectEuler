from time import time
from math import gcd

start = time()


class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.val = n / d

    def __gt__(self, other):
        return self.val > other.val

    def __st__(self, other):
        return self.val < other.val

    def __str__(self):
        return f"{self.n}/{self.d}"

    __repr__ = __str__

    def get_val(self):
        return self.val


max_d = 12000
fractions = []
for d in range(1, max_d + 1):
    for n in range(1, d):
        if gcd(n, d) == 1 and n != d:
            f = Fraction(n, d)
            if 1 / 3 < f.get_val() < 1 / 2:
                # print(f)
                fractions.append(f)

print(len(fractions))

print(f"Time: {time() - start:.3f}")