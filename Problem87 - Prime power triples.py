from time import time
from math import pow, ceil
start = time()


def sieve(n):
    is_prime = [None] * n
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    while p < n ** 0.5:
        is_prime[p] = True
        i = 2
        while i * p < n:
            is_prime[i * p] = False
            i += 1
        while True:
            p += 1
            if not p < n ** 0.5 or is_prime[p] == None:
                break
    for i in range(n):
        if is_prime[i] == None:
            is_prime[i] = True
    primes = []
    for i in range(n):
        if is_prime[i]:
            primes.append(i)
    return primes


limit = 50 * 10**6
squares = [p**2 for p in sieve(ceil(pow(limit, 1/2)))]
cubes = [p**3 for p in sieve(ceil(pow(limit, 1/3)))]
fourths = [p**4 for p in sieve(ceil(pow(limit, 1/4)))]

seen = set()
for p1 in squares:
    for p2 in cubes:
        for p3 in fourths:
            n = p1 + p2 + p3
            if n < limit:
                seen.add(n)
print(len(seen))
print(f"Time: {time() - start:.2f}")