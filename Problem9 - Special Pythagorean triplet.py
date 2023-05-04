x = False
for a in range(1, 500):
    for b in range(1, 500):
        if a + b + ((a**2+b**2)**0.5) == 1000:
            c = int((a**2+b**2)**0.5)
            print("{} + {} + {} = 1000\n{}*{}*{} = {}".format(a, b, c, a, b, c, a*b*c))
            x = True
        if x:
            break
