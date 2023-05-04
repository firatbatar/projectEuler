def isprime(number):
    if number == 1:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def numbers_of_divisor(number):
    divisors = 1
    i = 1
    if isprime(number):
        return divisors
    else:
        while i*i <= number:
            if number % i == 0:
                divisors += 1
                if number / i != i:
                    divisors += 1
            i += 1
        return divisors


def triangualar_numbers(term):
    triangualar_number = 0
    for i in range(0, term+1):
        triangualar_number += i
    return triangualar_number


n = 1
x = 1
while n <= 500:
    n = numbers_of_divisor(triangualar_numbers(x))
    x += 1
print(triangualar_numbers(x-1))
