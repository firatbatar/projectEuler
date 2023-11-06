from math import factorial
answer = 0
for i in range(3, 100000):
    temp = 0
    for n in str(i):
        temp += factorial(int(n))
        if temp > i:
            continue
    if temp == i:
        answer += i
print("Answer:", answer)
