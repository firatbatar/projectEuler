from time import time
from sympy import isprime
start = time()


def create_families(num):
    num = str(num)
    digits = []
    for digit in num:
        if digit not in digits:
            digits.append(digit)
    families = []
    for digit in digits:
        family = []
        for i in range(0, 10):
            if i != 0 or digit != num[0]:
                newNum = int(num.replace(digit, str(i)))
                if isprime(newNum):
                    family.append(newNum)
        family.sort()
        families.append(family)
    return families


num = 56003
cont = True
while cont:
    if not isprime(num):
        num += 1
        continue
    families = create_families(num)
    for family in families:
        if len(family) >= 8:
            cont = False
            print(family)
            print(f"Answer: {family[0]}")
            break
    num += 2
print("Time: {:.2f}".format(time() - start))
