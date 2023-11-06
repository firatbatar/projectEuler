from time import time
start = time()


def is_bouncy(num):
    num = [int(i) for i in list(str(num))]
    sorted = num.copy()
    sorted.sort()

    if num == sorted or num == sorted[::-1]:
        return False
    return True


bouncy_count = 21780 * 0.9
rate = None
n = 21780
while rate != 99:
    n += 1
    if is_bouncy(n):
        bouncy_count += 1
    rate = (bouncy_count / n) * 100

print(n)
print(f"Time: {time() - start:.2f}")
