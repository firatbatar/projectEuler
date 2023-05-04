from time import time, sleep


def is_pendigital(num):
    str_num = str(num)
    digit = len(str_num)
    check = True
    for i in range(1, digit+1):
        if str(i) in str_num:
            continue
        else:
            check = False
            break
    if check:
        return True
    else:
        return False


def isprime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


start = time()

n = 1
while True:
    if is_pendigital(n):
        if isprime(n):
            print(n)
    n += 1


print("Time {:.1f}".format(time() - start))
