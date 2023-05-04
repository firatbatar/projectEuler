def gen_triangle():
    n = 1
    while True:
        yield n * (n + 1) // 2
        n += 1


def gen_pentagonal():
    n = 1
    while True:
        yield n * (3*n - 1) // 2
        n += 1


def gen_hexagonal():
    n = 1
    while True:
        yield n * (2*n - 1)
        n += 1


triangle_gen = gen_triangle()
pentagonal = gen_pentagonal()
hexagonal = gen_hexagonal()
pentagonal_list = []
hexagonal_list = []
max_pentagonal = 0
max_hexagonal = 0

while True:
    triangle = next(triangle_gen)
    while triangle > max_pentagonal:
        max_pentagonal = next(pentagonal)
        pentagonal_list.append(max_pentagonal)
    while triangle > max_hexagonal:
        max_hexagonal = next(hexagonal)
        hexagonal_list.append(max_hexagonal)
    if triangle in pentagonal_list and triangle in hexagonal_list:
        print("Found", triangle)

