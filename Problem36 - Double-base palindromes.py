def dectobin(decnum):
    binnum = ""
    while not decnum == 0:
        i = decnum % 2
        binnum += str(i)
        decnum = decnum // 2
    binnum = binnum[::-1]
    return binnum


def ispalindrome(data):
    data_reverse = str(data)[::-1]
    if str(data) == data_reverse:
        return True
    return False


n = 1
answer = 0
while n < 1000000:
    if ispalindrome(n):
        if ispalindrome(dectobin(n)):
            answer += n
    n += 1
print(answer)
