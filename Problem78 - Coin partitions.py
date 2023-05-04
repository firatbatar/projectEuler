from time import time
start = time()

p = {0: 1}
n = 1
while True:
    m = 0
    penta = 1
    p[n] = 0
    while penta <= n:
        sign = -1 if m % 4 >= 2 else 1
        p[n] += sign * p[n - penta]

        m += 1

        k = int(m/2 + 1) if m % 2 == 0 else int(-(m/2 + 1))
        penta = k * (3*k - 1) / 2

    if p[n] % 10**6 == 0:
        break
    n += 1
print(n)
print(f"Time: {time() - start:.2f}")
