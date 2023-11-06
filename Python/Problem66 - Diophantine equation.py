# Solving Pelt's Equation with Continued Fractions By Jesse Unger
# Chakravala - a modern Indian method B.Sury
"""
For non-perfect square D, let m is the period of the continued fraction of sqrt(D) (Problem 64).
If m is even solution for the positive Pell's Equation is (x, y) = (p(m-1), q(m-1)), p and q being the numerator and denominator of the mth estimate fraction.
If m is odd then (x, y) = (p(m-1), q(m-1)) is the solution for the negative Pell's Equation.
By Baskara's Lemma for the solution of an negative Pell's equation (x, y), (2 * x^2 + 1, 2*x*y) is the solution for the positve Pell's equation.
"""


from time import time
from math import floor, sqrt
start = time()


def period_length(n):
    a0 = floor(sqrt(n))

    if a0 == sqrt(n):
        return 0

    a = a0
    m = a0
    d = n - a0**2
    seen = {}
    idx = 0
    a_dict = {}

    while (a, m, d) not in seen:
        seen[(a, m, d)] = idx
        a_dict[idx] = a
        a = (a0 + m) // d
        m = d * a - m
        d = (n - m**2) // d
        idx += 1

    return a_dict


def find_numerator(a_dict):
    a_list = list(a_dict.values())[:-1]
    numerator = 1
    denominator = a_list.pop()
    while a_list:
        denominator, numerator = denominator * a_list.pop() + numerator, denominator
    return numerator


x_dict = {}
for D in range(1000+1):
    period = period_length(D)
    if period == 0:
        continue

    period_len = len(period)-1
    possible_x = find_numerator(period)
    if period_len % 2 == 0:
        x_dict[possible_x] = D
    else:
        x_dict[2 * possible_x**2 + 1] = D

# print(x_list)
max_x = max(x_dict.keys())
answer = x_dict[max_x]
print(f"Answer: {answer} (max x is {max_x})")
print(f"Time: {time()-start:.2f}")
