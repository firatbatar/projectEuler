from time import time
from math import sqrt, floor
start = time()


def period_length(n):
    a0 = floor(sqrt(n))

    if a0 == sqrt(n):
        return 0

    a = a0
    m = a0
    d = n - a0**2
    seen = {}
    idx = 0
    while (a, m, d) not in seen:
        seen[(a, m, d)] = idx
        a = (a0 + m) // d
        m = d * a - m
        d = (n - m**2) // d
        idx += 1

    return idx


counter = 0
for num in range(2, 10001):
    period = period_length(num)
    if period != 0 and period % 2 == 0:
        counter += 1
print(counter)

print(f"Time: {time()-start:.2f}")
