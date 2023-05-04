from time import time
from math import gcd
start = time()


""" SLOW VERSION
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


def relative_primes(num1, num2):
    if num1 == num2:
        return False
    for i in primes:
        if i > num1 or i > num2:
            break
        if num1 % i == 0 and num2 % i == 0:
            return False
    return True


def relative_primes_2(num1, num2):
    return gcd(num1, num2) == 1


def totient(n):
    r_primes = []
    step = 1
    if n % 2 == 0:
        step = 2
    for i in range(1, n, step):
        if relative_primes_2(n, i):
            r_primes.append(i)
    return len(r_primes)


def totient_2(n):
    ps = []
    tot = n
    for prime in primes:
        if prime > n:
            break
        if n % prime == 0:
            ps.append(prime)
    for p in ps:
        tot *= (1 - (1 / p))
    return int(tot)


primes = sieve(10**6)
maxa = 0
maxn = 0
n = 2
while n <= 10**6:
    a = n / totient_2(n)
    # print(n)
    if a > maxa:
        maxa = a
        maxn = n
        print(n, "---")
        if n == 510510:
            print(f"Time: {time() - start:.3f}")
    n += 2
print(maxn)
# print(totient_2(98))"""


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


def solution(limit):
    answer = 1
    primes = sieve(100)
    i = 0
    while primes[i] * answer <= limit:
        answer *= primes[i]
        i += 1
    return answer


print(solution(10**6))
print(f"Time: {time() - start:.3f}")
