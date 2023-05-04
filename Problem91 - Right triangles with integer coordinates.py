from time import time
start = time()

limit = 50
triangles = []

for x1 in range(limit+1):
    for y1 in range(limit+1):
        for x2 in range(limit+1):
            for y2 in range(limit+1):
                if x1 == y1 == 0 or x2 == y2 == 0:
                    continue
                if (x1, y1) == (x2, y2):
                    continue
                if (x1 == x2 == 0) or (y1 == y2 == 0):
                    continue
                magic_sum = x1*x2 + y1*y2

                if magic_sum == 0 or magic_sum == x1**2 + y1**2 or magic_sum == x2**2 + y2**2:
                    tri = [(x1, y1), (x2, y2)]
                    tri.sort()
                    if tri not in triangles:
                        triangles.append(tri)

print(len(triangles))
print(f"Time: {time() - start:.2f}")
