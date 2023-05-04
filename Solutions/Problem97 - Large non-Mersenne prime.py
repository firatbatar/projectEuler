from time import time
start = time()

num = (28433 * (2 ** 7830457)) + 1
answer = ""
for i in range(10):
    answer += str(num % 10)
    num //= 10

print(answer[::-1])
print(f"Time: {time() - start:.3f}")
