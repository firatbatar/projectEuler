import time
start = time.time()

nums = [str(x) for x in range(1, 10)]
productOld = 0
for num in range(1, 9328):
    something = 0
    n = 1
    product = ""
    while True:
        product += str(num * n)
        for i in nums:
            if product.count(i) == 1:
                if i == "9":
                    something = num
                    break
                continue
            elif product.count(i) > 1 or len(product) >= 9:
                something = -1
                break
            else:
                break
        if something != 0:
            break
        else:
            n += 1
    if something == -1:
        continue
    else:
        if productOld < int(product):
            productOld = int(product)
print("Answer: " + product)
print("Time: {:.2f}".format(time.time() - start))
