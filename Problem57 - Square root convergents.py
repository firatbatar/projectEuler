from time import time
from fractions import *
import sys
sys.setrecursionlimit(1500)

start = time()


def find_denominator(iteration):
    if iteration == 1:
        return 2 + Fraction(1, 2)
    else:
        return 2 + Fraction(1, find_denominator(iteration - 1))


def fraction(iteration):
    if iteration == 1:
        return 1 + Fraction(1, 2)
    else:
        return 1 + Fraction(1, find_denominator(iteration - 1))


counter = 0

for i in range(1, 10**3):
    frac = str(fraction(i))
    numerator, denomintor = frac.split('/')

    if len(numerator) > len(denomintor):
        counter += 1

    # print(frac, '\n')

print(counter)
print('Time: {:.2f}'.format(time() - start))
