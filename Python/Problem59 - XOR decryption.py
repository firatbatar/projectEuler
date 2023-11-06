"""
An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum"
[On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire
sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum
of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of
this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of
this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon
show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six,
and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter
of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered
that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely,
the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle
whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series
in which the exponents are even numbers.
"""
with open('../txt/p059_cipher.txt', 'r') as file:
    encrypted = file.read()
letters = encrypted.split(',')
pile1 = []
pile2 = []
pile3 = []

for i in range(0, len(letters), 3):
    pile1.append(int(letters[i]))
for i in range(1, len(letters), 3):
    pile2.append(int(letters[i]))
for i in range(2, len(letters), 3):
    pile3.append(int(letters[i]))


def most_frequent(pile):
    letters = dict()
    for i in pile:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    most = None
    temp = 0
    for i, j in letters.items():
        if j > temp:
            temp = j
            most = i
    return most


def dencryption(pile, key):
    encrypted = []
    for i in pile:
        encrypted.append(i ^ key)
    return encrypted


most1 = most_frequent(pile1)
key1 = 32 ^ most1
most2 = most_frequent(pile2)
key2 = 32 ^ most2
most3 = most_frequent(pile3)
key3 = 32 ^ most3
dencrypted1 = dencryption(pile1, key1)
dencrypted2 = dencryption(pile2, key2)
dencrypted3 = dencryption(pile3, key3)
text = ""
for i in range(len(pile1)):
    text += chr(dencrypted1[i])
    text += chr(dencrypted2[i])
    text += chr(dencrypted3[i])
# print(text)
answer = sum(dencrypted1) + sum(dencrypted2) + sum(dencrypted3)
print(answer)


