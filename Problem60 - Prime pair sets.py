from sympy import isprime
from time import time
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


def check(a, b):
    a, b = str(a), str(b)
    num1 = int(a + b)
    num2 = int(b + a)
    return isprime(num1) and isprime(num2)


def main(primes):
    for a in primes:
        for b in primes:
            if b < a:
                continue
            if check(a, b):
                for c in primes:
                    if c < b:
                        continue
                    if check(a, c) and check(b, c):
                        for d in primes:
                            if d < c:
                                continue
                            if check(a, d) and check(b, d) and check(c, d):
                                for e in primes:
                                    if e < d:
                                        continue
                                    if check(a, e) and check(b, e) and check(c, e) and check(d, e):
                                        return a + b + c + d + e


primes = sieve(10 ** 4)
print(main(primes))
print("Time: {:.2f}".format(time() - start))


