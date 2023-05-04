from time import time
start = time()


def count_rect(m, n):
    return m * (m+1) * n * (n+1) / 4


m = 2000
n = 1
target = 2000000
error = float('inf')
answer = None

while m >= n:
    rects = count_rect(m, n)
    err = abs(rects - target)

    if error > err:
        error = err
        answer = m * n

    if rects > target:
        m -= 1
    else:
        n += 1

print(f"{answer}")
print(f"Time: {time() - start:.2f}")
