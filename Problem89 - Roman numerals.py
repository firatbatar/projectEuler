from time import time

start = time()


def dec_to_roman(num: int):
    if num == 0:
        return ""

    if num >= 1000:
        return "M" + dec_to_roman(num - 1000)
    elif num >= 900:
        return "CM" + dec_to_roman(num - 900)
    elif num >= 500:
        return "D" + dec_to_roman(num - 500)
    elif num >= 400:
        return "CD" + dec_to_roman(num - 400)
    elif num >= 100:
        return "C" + dec_to_roman(num - 100)
    elif num >= 90:
        return "XC" + dec_to_roman(num - 90)
    elif num >= 50:
        return "L" + dec_to_roman(num - 50)
    elif num >= 40:
        return "XL" + dec_to_roman(num - 40)
    elif num >= 10:
        return "X" + dec_to_roman(num - 10)
    elif num >= 9:
        return "IX" + dec_to_roman(num - 9)
    elif num >= 5:
        return "V" + dec_to_roman(num - 5)
    elif num >= 4:
        return "IV" + dec_to_roman(num - 4)
    elif num >= 1:
        return "I" + dec_to_roman(num - 1)


def roman_to_dec(num: str):
    numeral_values = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
                      "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    value = 0
    for numeral in numeral_values.keys():
        value += numeral_values[numeral] * num.count(numeral)
        num = num.replace(numeral, "")

    return value


with open("p089_roman.txt", "r") as file:
    romans = [i.replace("\n", "") for i in file.readlines()]

saved = 0
for roman in romans:
    dec = roman_to_dec(roman)
    best = dec_to_roman(dec)
    saved += len(roman) - len(best)

print(saved)
print(f"Time: {time() - start:.2f}")
