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


upper_limit = 100
primes = sieve(upper_limit)
ways = [1] + [0]*upper_limit

for i in primes:
    for j in range(i, len(ways)):
        ways[j] += ways[j - i]

for i in range(len(ways)):
    if ways[i] > 5000:
        print(i)
        break
print(f"Time: {time() - start:.2f}")
