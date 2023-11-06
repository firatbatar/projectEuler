from time import time
import math
start = time()


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_prime_2(n):
    global memo

    if n == 1:
        return False

    temp = math.sqrt(n)
    for i in memo:
        if i > temp:
            break
        if n % i == 0:
            return False
    memo.append(n)
    return True


memo = [2]
n = 3
x = 1
while x != 10002:
    if is_prime_2(n):
        x += 1
        n += 1
    else:
        n += 1
print(n-1)
print(f"Time: {time() - start}")
