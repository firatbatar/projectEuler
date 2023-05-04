from time import time
from math import factorial
start = time()


def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


answer = 0
for n in range(23, 101):
    for r in range(n, 1, -1):
        if combination(n, r) > 10**6:
            answer += 1

print(answer)
print("Time: {:.2f}".format(time() - start))
