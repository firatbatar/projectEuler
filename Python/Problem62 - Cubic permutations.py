from time import time
start = time()

num = 0
cubes = []
while True:
    cube = sorted(list(str(num ** 3)))
    cubes.append(cube)
    if cubes.count(cube) == 5:
        print(cubes.index(cube))
        print(cubes.index(cube) ** 3)
        break
    num += 1
print("Time: {:.2f}".format(time() - start))

