counter = 0
for num in range(1, 10):
    power = 1
    while True:
        digit = len(str(num**power))
        if digit == power:
            print(f"{num}^{power}={num**power} ({digit})")
            counter += 1
            power += 1
        else:
            break

print(f"Answer: {counter}")
