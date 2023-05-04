from time import time
start = time()


def totient_sieve(n):
    is_prime = [True] * (n + 1)
    totients = list(range(n + 1))

    for p in range(2, n+1):
        if not is_prime[p]:
            continue
        for i in range(p, n+1, p):
            is_prime[i] = False
            totients[i] = int(totients[i] * (1 - 1/p))

    return totients


def is_perm(n1, n2):
    n1 = list(str(n1))
    n1.sort()
    n2 = list(str(n2))
    n2.sort()
    return n1 == n2


limit = 10**7
tots = totient_sieve(limit)
perm_tots = [n/tots[n] if is_perm(n, tots[n]) else float('inf') for n in range(2, limit+1)]
# print(min(perm_tots))
print(perm_tots.index(min(perm_tots)) + 2)
print(f"Time: {time() - start:.2f}")
