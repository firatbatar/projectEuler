from time import time
from math import log

start = time()

with open("../txt/p099_base_exp.txt") as file:
    base_exp = file.readlines()

for i in range(len(base_exp)):
    data = base_exp[i].replace("\n", "")
    base_exp[i] = data.split(",")

max_index = 0
max_number = log(int(base_exp[0][0])) * int(base_exp[0][1])
for i in range(len(base_exp)):
    if i == max_index:
        continue

    base = log(int(base_exp[i][0]))
    exp = int(base_exp[i][1])

    new_number = base * exp

    if new_number > max_number:
        max_index = i
        max_number = new_number

print(max_index + 1)
print(f"{time() - start:.3f}")