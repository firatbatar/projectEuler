from time import time
start = time()


def prime_factors(number):
    i = 2
    prime_factor = set()
    while i < number**0.5:
        while number % i == 0:
            prime_factor.add(i)
            number //= i
        i += 1
    return len(prime_factor) + 1


n = 210
while True:
    check = True
    for i in range(n, n+4):
        if prime_factors(i) == 4:
            continue
        else:
            check = False
            break
    if check:
        print(n)
        print("Time: {:.2f}".format(time() - start))
        break
    n += 1

