from time import time
from sympy import isprime
start = time()


# def isprime(n):
#     if n == 1:
#         return False
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True
#
#
# def gen_composite_odd():
#     n = 3
#     while True:
#         if not isprime(n):
#             yield n
#         n += 2
#
#
# def find_next(i, j, dif):
#     if i == 0 and j == 0 and dif == 0:
#         return 2, 1, 0
#     if i == 2:
#         new_i = 3
#     else:
#         new_i = i + 2
#         while not isprime(new_i):
#             new_i += 2
#     new_j = j + 1
#     dif += new_i - i
#     if dif < 2*(new_j**2):
#         return new_i, j, dif
#     return 2, new_j, 0
#
#
# def create_next(i, j, dif):
#     while True:
#         i, j, dif = find_next(i, j, dif)
#         return i + 2*(j**2), i, j, dif
#
#
# odd_composite_gen = gen_composite_odd()
# odd_composite = list()
# odd_composite.append(next(odd_composite_gen))
# odd_composite.append(next(odd_composite_gen))
# odd_composite.append(next(odd_composite_gen))
#
# i = 0
# j = 0
# dif = 0
# while True:
#     current_max = odd_composite[-1]
#     new_number, i, j, dif = create_next(i, j, dif)
#     if new_number % 2 == 0 or isprime(new_number):
#         continue
#     while current_max < new_number:
#         odd_composite.append(next(odd_composite_gen))
#         current_max = odd_composite[-1]
#     print(new_number, current_max)
#     if new_number not in odd_composite:
#         break
#
# print(new_number)
# print("Time: {:.2f}".format(time() - start))
#
# i = 0
# j = 0
# dif = 0
# golbach_nums = list()
# for n in range(3000):
#     new_golbach, i, j, dif = create_next(i, j, dif)
#     if new_golbach % 2 != 0 and not isprime(new_golbach):
#         golbach_nums.append(new_golbach)
# print(golbach_nums)
#
# composite_odd_gen = gen_composite_odd()
# while True:
#     next_composite = next(composite_odd_gen)
#     if next_composite > golbach_nums[-1]:
#         print("Liste Yetmedi.")
#         break
#     if next_composite not in golbach_nums:
#         print(next_composite)
#         print("Time: {:.2f}".format(time() - start))
#         break


number = 9
while True:
    if isprime(number):
        number += 2
        continue
    ok = False
    j = 1
    while True:
        i = number - 2*(j**2)
        if isprime(i):
            ok = True
            break
        elif i < 1:
            break
        j += 1
    if not ok:
        print(number)
        print("Time: {:.2f}".format(time() - start))
        break
    number += 2
