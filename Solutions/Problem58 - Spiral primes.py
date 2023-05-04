from time import time
from sympy import isprime
start = time()


def gen_corners():
    length = 3
    while True:
        bottom_right = length ** 2
        bottom_left = bottom_right - (length - 1)
        top_left = bottom_left - (length - 1)
        top_right = top_left - (length - 1)
        yield [bottom_right, bottom_left, top_right, top_left], length
        length += 2


def corner_primes(corner_list):
    primes = []
    for i in corner_list:
        if isprime(i):
            primes.append(i)
    return primes


# corners = create_corners(7)
# answer = calculate_percent(corners)
# print(answer)

corner_gen = gen_corners()
new_corners, length = next(corner_gen)
corners = [1] + new_corners
new_corners, length = next(corner_gen)
corners += new_corners
new_corners, length = next(corner_gen)
corners += new_corners
primes = corner_primes(corners)
percent = (len(primes) / len(corners)) * 100
while True:
    new_corners, length = next(corner_gen)
    corners += new_corners
    primes += corner_primes(new_corners)
    percent = (len(primes) / len(corners)) * 100
    if percent <= 10:
        break

print(percent, length)
print("Time: {:.2f}".format(time() - start))


