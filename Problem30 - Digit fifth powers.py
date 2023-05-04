answer = []
for i in range(2, 1000000):
    temp = 0
    for n in str(i):
        temp += int(n)**5
        if temp > i:
            continue
    if temp == i:
        answer.append(i)
print("Answer:", sum(answer))
