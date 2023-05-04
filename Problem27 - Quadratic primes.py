import time


def isprime(number):
    if number == 1:
        return False
    if number == 0:
        return False
    if number < 0:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def quadratic_primes(a, b):
    if not isprime(b):
        return 0
    counter = 0
    for n in range(0, 10 ** 5):
        number = n ** 2 + a * n + b
        if isprime(number):
            counter += 1
        else:
            break
    return counter


counter_max = 0
a_max = 0
b_max = 0
for a in range(-999, 1000):
    for b in range(0, 1001):
        if quadratic_primes(a, b) > counter_max:
            counter_max = quadratic_primes(a, b)
            a_max = a
            b_max = b

print(counter_max, a_max*b_max)
start_time = time.time()
