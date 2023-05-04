def letter_count(number):
    birler = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    onlar = [0, [3, 6, 6, 8, 8, 7, 7, 9, 8, 8], 6, 6, 5, 5, 5, 7, 6, 6]
    lettercount = 0
    if len(str(number)) == 1:
        lettercount += birler[number]
        return lettercount
    elif len(str(number)) == 2:
        if int(str(number)[0]) == 1:
            lettercount += onlar[1][int(str(number)[1])]
            return lettercount
        else:
            lettercount += onlar[int(str(number)[0])]
            lettercount += birler[int(str(number)[1])]
            return lettercount
    elif len(str(number)) == 3:
        lettercount += birler[int(str(number)[0])] + 7
        if int(str(number)[1]) == 0 and int(str(number)[2]) == 0:
            return lettercount
        else:
            lettercount += 3
            if int(str(number)[1]) != 1:
                lettercount += onlar[int(str(number)[1])]
                lettercount += birler[int(str(number)[2])]
                return lettercount
            else:
                lettercount += onlar[1][int(str(number)[2])]
                return lettercount


answer = 11
for i in range(1, 1000):
    answer += letter_count(i)
print(answer)
