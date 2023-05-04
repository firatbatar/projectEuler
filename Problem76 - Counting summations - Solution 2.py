from time import time
start = time()

p = {0: 1}
for n in range(1, 101):
    m = 0
    penta = 1
    p[n] = 0
    while penta <= n:
        sign = -1 if m % 4 >= 2 else 1
        p[n] += sign * p[n - penta]

        m += 1

        k = int(m/2 + 1) if m % 2 == 0 else int(-(m/2 + 1))
        penta = k * (3*k - 1) / 2

print(p[100] - 1)
print(f"Time: {time() - start:.2f}")
