from time import time
start = time()


def isprime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main_number():
    primes = [2]
    n = 3
    while sum(primes) < 10**6:
        if isprime(n):
            primes.append(n)
        n += 2
    primes.pop()
    return primes


def pop_end(primes):
    while True:
        sum_of_primes = sum(primes)
        if isprime(sum_of_primes):
            return f"Prime: {sum_of_primes}", f"Terms len: {len(primes)}"
        primes.remove(primes[-1])


def pop_start(primes):
    while True:
        sum_of_primes = sum(primes)
        if isprime(sum_of_primes):
            return f"Prime: {sum_of_primes}", f"Terms len: {len(primes)}"
        primes.pop(0)


number = main_number()
number1 = main_number()
print(pop_start(number1))
print("Time: {:.2f}".format(time() - start))
print(pop_end(number))
print("Time: {:.2f}".format(time() - start))
