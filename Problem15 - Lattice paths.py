def factorial(number):
    factorial = 1
    for i in range (1,number+1):
        factorial *= i
    return factorial


def combination(n, r):
    combination = int(factorial(n)/(factorial(r)*factorial(n-r)))
    return combination


print(combination(40, 20))
