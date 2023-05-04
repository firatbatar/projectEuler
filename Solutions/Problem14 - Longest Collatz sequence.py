from time import time
start = time()


def collatz(star_num):
    current_num = star_num
    terms = 1
    while current_num != 1:
        if current_num % 2 == 0:
            current_num = int(current_num/2)
            terms += 1
        else:
            current_num = int(3*current_num + 1)
            terms += 1
    return terms


max_terms = 0
max_terms_start = 1
for i in range(1, 1000000):
    if collatz(i) > max_terms:
        max_terms = collatz(i)
        max_terms_start = i
print(max_terms_start)
print(f"Time: {time()-start:.2f}")
