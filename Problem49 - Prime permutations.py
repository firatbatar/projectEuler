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


for number in range(1000, 9999):
    if not isprime(number):
        continue

    number_list = list(str(number))
    number2 = number + 3330
    number2_list = list(str(number2))
    number_list.sort()
    number2_list.sort()
    if number_list != number2_list or not isprime(number2) or len(str(number2)) > 4:
        continue

    number3 = number2 + 3330
    number3_list = list(str(number3))
    number3_list.sort()
    if number_list != number3_list or not isprime(number3) or len(str(number2)) > 4:
        continue

    print(number, number2, number3)
    print(str(number) + str(number2) + str(number3))
    print("Time: {:.2f}".format(time() - start))
