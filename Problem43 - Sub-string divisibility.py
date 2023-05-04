from time import time
start = time()


def permutation(data):
    if len(data) == 1:
        return data
    permutations = []
    for n in data:
        n1 = data.replace(n, "")
        n2 = permutation(n1)
        for k in n2:
            permutations.append(n + k)
    return permutations


def pattern(num):
    if num[0] == "0":
        return False
    primes = [17, 13, 11, 7, 5, 3, 2]
    num = str(num)
    start_index = 7
    for i in primes:
        little_num = num[start_index:start_index+3]
        if int(little_num) % i != 0:
            return False
        start_index -= 1
    return True


start_num = "0123456789"
answer = 0
for num in permutation(start_num):
    if pattern(num):
        answer += int(num)

print(f"Answer: {answer}\n")
print("Time: {:.2f}".format(time() - start))