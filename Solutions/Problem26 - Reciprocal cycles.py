import time
start_time = time.time()


def devirli(denominator, numerator):
    number = numerator // denominator
    snumber = str(number)
    rsnumber = snumber[::-1]
    if rsnumber[0] == "0":
        return 0
    for i in range(1, len(rsnumber)):
        a = rsnumber[:i]
        b = rsnumber[i:2*i]
        if a == b:
            return len(a)
    return 0


answer = 0
devir = 0
numerator = 10 ** 10000
for i in range(2, 1000):
    if devirli(i, numerator) > devir:
        answer = i
        devir = devirli(i, numerator)
print(answer)
print(time.time() - start_time)
