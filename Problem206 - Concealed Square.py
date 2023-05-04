from time import time
from math import sqrt, ceil
start = time()


def check_form(num):
    strNum = str(num)
    return all(int(strNum[x*2]) == x+1 for x in range(9))


# num = 138902663
num = ceil(sqrt(19293949596979899))
while not check_form(num ** 2):
    num -= 2
print(num * 10)
print(f"Time: {time() - start:.3f}")

