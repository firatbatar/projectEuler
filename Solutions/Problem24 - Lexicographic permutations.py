from itertools import permutations

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation = []
for i in permutations(numbers):
    number = ""
    for n in i:
        number += str(n)
    permutation.append(number)
permutation.sort()
print(permutation[999999])