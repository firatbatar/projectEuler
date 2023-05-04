from time import time
from math import gcd
start = time()

d = 10 ** 6 // 7
while True:
    if gcd(7 * d, (3 * d) - 7) == 1:
        break
    d -= 1
print((3 * d) - 1)
print(f"Time: {time() - start:f}")
