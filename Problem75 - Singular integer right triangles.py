from time import time
from math import gcd
start = time()

triples = set()
for n in range(1, 866):
    for m in range(n+1, 867):
        if gcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0):
            a = m**2 + n**2
            b = 2*m*n
            c = m**2 - n**2
            triples.add((a, b, c))

vals = dict()
for triple in triples:
    i = 1
    L = sum(triple)
    while L * i <= 1500000:
        if L * i in vals:
            vals[L*i] += 1
        else:
            vals[L*i] = 1
        i += 1

answer = 0
for val in vals.values():
    if val == 1:
        answer += 1
print(answer)
print(f"Time: {time() - start:.2f}")
