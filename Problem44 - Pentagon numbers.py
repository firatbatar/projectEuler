from time import time
from math import sqrt
start = time()


def pentagonal_number(n):
    return n * (3*n - 1) // 2


def is_pentagonal(num):
    n = (1 + sqrt(1 + 24*num)) / 6
    return n.is_integer()


for i in range(1, 10**4):
    for j in range(i-1, 0, -1):
        pentagonal_1 = pentagonal_number(i)
        pentagonal_2 = pentagonal_number(j)
        if is_pentagonal(pentagonal_1 + pentagonal_2) and is_pentagonal(pentagonal_1 - pentagonal_2):
            print("Answer: ", pentagonal_1 - pentagonal_2)
            print("Time: {:.2f}".format(time() - start))