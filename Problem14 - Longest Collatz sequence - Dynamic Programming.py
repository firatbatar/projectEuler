"""
Collatz Sequance:
next_n = {
            n/2 if n is even,
            3n + 1 if n is odd
        }
If n is 1 it finishes.
Which starting number, under one million, produces the longest chain?
"""

from time import time

start = time()


def collazt(n):
    global memo

    if n in memo:
        return memo[n]
    if n == 1:
        return 1

    if n % 2 == 0:
        next_n = n//2
        memo[n] = 1 + collazt(next_n)
        return memo[n]
    else:
        next_n = (3*n + 1)//2
        memo[n] = 2 + collazt(next_n)
        return memo[n]


longest_chain = -1
longest_n = None
memo = dict()
for n in range(1, 10**9):
    c = collazt(n)
    if c > longest_chain:
        longest_chain = c
        longest_n = n

print(longest_n)
print(f"Time: {time() - start}")
