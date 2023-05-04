def isdivisible(number):
    for x in range(2, 21):
        if number % x != 0:
            return False
    return True


primes = {2, 3, 5, 7, 11, 13, 17, 19}
num = 1
for i in primes:
    num *= i

while True:
    if isdivisible(num):
        print(num)
        break
    num += 1
