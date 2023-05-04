# e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 2k, 1, ..]
from time import time

start = time()


def find_e(i, d=0, n=1):
    if i == 0:
        return 2 * d + n, d

    k = 1
    if i % 3 == 2:
        k = ((i // 3) + 1) * 2

    if d == 0:
        d = k
        return find_e(i - 1, d, n)

    n += k * d
    d, n = n, d
    return find_e(i - 1, d, n)


n = 100
a, b = find_e(n - 1)
print(sum([int(i) for i in list(str(a))]))
print(f"Time: {time() - start:.3f}")