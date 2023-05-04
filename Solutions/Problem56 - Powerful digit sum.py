from time import time
start = time()


def sum_of_digits(num):
    str_num = str(num)
    digit_sum = 0
    for i in str_num:
        digit_sum += int(i)
    return digit_sum


best = 0
for a in range(1, 100):
    for b in range(1, 100):
        if best < sum_of_digits(a ** b):
            best = sum_of_digits(a ** b)

print(best)
print("Time: {:.2f}".format(time() - start))
