from time import time
start = time()

target = 100
ways = [1] + [0]*target

for i in range(1, target+1):
    for j in range(i, target+1):
        ways[j] += ways[j - i]

print(ways[-1] - 1)
print(f"Time: {time() - start:.2f}")
