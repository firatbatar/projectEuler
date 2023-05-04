def isprime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def istruncatable_ltr(number):
    temp = str(number)
    while len(temp) != 0:
        if not isprime(int(temp)):
            return False
        temp = temp[1:]
    return True


def istruncatable_rtl(number):
    temp = str(number)
    while len(temp) != 0:
        if not isprime(int(temp)):
            return False
        temp = temp[:len(temp)-1]
    return True


liste = []
for i in range(8, 1000000):
    if istruncatable_ltr(i) and istruncatable_rtl(i):
        liste.append(i)
print(sum(liste))
