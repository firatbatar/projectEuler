from time import time
start = time()


def chain(start):
    start = str(start)
    new = 0
    for i in start:
        new += int(i)**2
    if new == 89:
        return True
    elif new == 1:
        return False
    else:
        return chain(new)


counter = 0
for i in range(1, 10**7):
    # print(i)
    if chain(i):
        counter += 1

print(f"Answer: {counter}")
print("Time {:.2f}".format(time()-start))
