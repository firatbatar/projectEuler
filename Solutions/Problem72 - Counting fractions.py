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


limit = 10**6
answer = sum(totient_sieve(limit)[2:])
print(answer)
print(f"Time: {time() - start:.2f}")
