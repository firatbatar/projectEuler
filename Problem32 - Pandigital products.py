import time
start = time.time()


def ispandigital(multiplicand, multiplier, product):
    test = "123456789"
    number = sorted(str(multiplicand) + str(multiplier) + str(product))
    num = "".join(str(i) for i in number)
    return test == num


products = []
for multiplicand in range(1, 10000):
    for multiplier in range(1, 10000):
        if ispandigital(multiplicand, multiplier, multiplier*multiplicand):
            if multiplier*multiplicand not in products:
                products.append(multiplier*multiplicand)
print("Products:", products)
print("Answer:", sum(products))
print(time.time() - start)
