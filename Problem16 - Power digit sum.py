def sum_of_digits(num):
    sumofdigits = 0
    for i in str(num):
        sumofdigits += int(i)
    return sumofdigits


print(sum_of_digits(2**1000))