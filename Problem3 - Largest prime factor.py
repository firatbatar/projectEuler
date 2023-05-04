from time import time
start = time()


def isprime(num):
    if num <= 1:
        return False
    if num % 2 == 0:
        return False

    i = 3
    while i*i < num:
        if num % i == 0:
            return False
        i += 2
    return True


def primefactors(num):

    if num % 2 == 0:
        largestprimefactor = [2]
    else:
        largestprimefactor = []
    i = 3
    num_copy = num
    while i*i < num:
        if isprime(i):
            if num_copy % i == 0:
                largestprimefactor.append(i)
            while num_copy % i == 0:
                num_copy /= i
        i += 2
    return largestprimefactor[-1]


print(primefactors(600851475143))
print("Time: {:.2f}".format(time() - start))
