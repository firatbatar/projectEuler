def ispalindrome(data):
    data_reverse = str(data)[::-1]
    if str(data) == data_reverse:
        return True
    return False


counter = 0
for n in range(1, 10000):
    num = str(n)
    for turn in range(1, 50):
        reverseNum = num[::-1]
        total = int(num) + int(reverseNum)
        reverseTotal = int(str(total)[::-1])
        if total == reverseTotal:
            print(n, total, turn)
            counter += 1
            break
        else:
            num = str(total)

print(f"Answer: {9999-counter}")
