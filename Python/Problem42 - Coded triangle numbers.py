from time import time
start = time()

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

with open("../../txt/words.txt", "r") as file:
    words = file.read().split(",")

triangle_nums = list()
for n in range(1, 500):
    tn = 1/2 * n * (n + 1)
    triangle_nums.append(tn)

count = 0


for word in words:
    value = 0
    for letter in word:
        value += alphabet.index(letter) + 1
    if value in triangle_nums:
        count += 1

print(count)
print("Time: {:.2f}".format(time() - start))
