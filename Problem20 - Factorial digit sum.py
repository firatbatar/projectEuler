def factorial(number):
    factorial = 1
    for i in range (1,number+1):
        factorial *= i
    return factorial


def sum_of_digits(num):
    sumofdigits = 0
    for i in str(num):
        sumofdigits += int(i)
    return sumofdigits


print(sum_of_digits(int(factorial(100))))