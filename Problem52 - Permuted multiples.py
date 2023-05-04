from time import time
start = time()


def is_permuted(num1, num2):
    num1 = list(str(num1))
    num2 = list(str(num2))
    num1.sort()
    num2.sort()
    return num1 == num2


number = 0
while True:
    number += 1
    if not is_permuted(number, 2*number):
        continue
    if not is_permuted(number, 3*number):
        continue
    if not is_permuted(number, 4*number):
        continue
    if not is_permuted(number, 5*number):
        continue
    if not is_permuted(number, 6*number):
        continue
    print(number)
    print("Time: {:.2f}".format(time() - start))
    break
