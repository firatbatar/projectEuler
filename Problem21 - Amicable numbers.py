def sum_of_proper_divisors(num):
    sumofdivisors = 0
    for i in range(1, num):
        if num % i == 0:
            sumofdivisors += i
    return sumofdivisors


def is_amicable(num):
    if sum_of_proper_divisors(sum_of_proper_divisors(num)) == num:
        if sum_of_proper_divisors(num) == num:
            return False
        else:
            return True
    else:
        return False


sum_of_amicable_numbers = 0
for i in range(1, 10000):
    if is_amicable(i):
        print(i)
        sum_of_amicable_numbers += i
print(sum_of_amicable_numbers)
