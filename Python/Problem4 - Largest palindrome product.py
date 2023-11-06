def largestpolindrome():
    largestpalindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            sayi = i * j
            if str(sayi) == str(sayi)[::-1]:
                largestpalindrome = max(sayi, largestpalindrome)
    return largestpalindrome


print(largestpolindrome())
