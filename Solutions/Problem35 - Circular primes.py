def isprime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


primes = []
number = 2
while number < 1000000:
    temp = str(number)
    for i in temp:
        if not isprime(int(temp)):
            break
        temp = temp[1:] + i
        if int(temp) == number:
            if number not in primes:
                primes.append(number)
    number += 1
print(len(primes))
