from time import time
start = time()
a = ""
n = 1
while n < 1000001:
    a += str(n)
    n += 1
answer = int(a[0]) * int(a[9]) * int(a[10**2 - 1]) * int(a[10**3 - 1]) * int(a[10**4 - 1]) * int(a[10**5 - 1]) * int(a[10**6 - 1])
print(answer)

print("Time: {:.2f}".format(time() - start))