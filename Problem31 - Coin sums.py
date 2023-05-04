import time
start = time.time()
# coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]


def check(pound2, pound1, pence50, pence20, pence10, pence5, pence2, pence1):
    return (pound2*200) + (pound1*100) + (pence50*50) + (pence20*20) + (pence10*10) + (pence5*5) + (pence2*2) + (pence1*1) == 200


counter = 0
for pound2 in range(0, 1+1):
    if pound2 == 1:
        counter += 1
        break
    for pound1 in range(0, 2+1):
        for pence50 in range(0, 4+1):
            for pence20 in range(0, 10+1):
                for pence10 in range(0, 20+1):
                    for pence5 in range(0, 40+1):
                        for pence2 in range(0, 100+1):
                            for pence1 in range(0, 200+1):
                                if check(pound2, pound1, pence50, pence20, pence10, pence5, pence2, pence1):
                                    counter += 1
                                    print(counter)
print(counter)
print(time.time() - start)
