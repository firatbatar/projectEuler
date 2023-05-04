from time import time
start = time()


def is_contain_origin(tri):
    x1, y1 = tri[0][0], tri[0][1]
    x2, y2 = tri[1][0], tri[1][1]
    x3, y3 = tri[2][0], tri[2][1]

    real_area = abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)) / 2

    # 3 areas with one point as origin
    area_1 = abs((x2*y3) - (x3*y2)) / 2
    area_2 = abs((x3*y1) - (x1*y3)) / 2
    area_3 = abs((x1*y2) - (x2*y1)) / 2

    # If the real area is equal to the sum of three areas, then point is inside the triangle
    return real_area == area_1 + area_2 + area_3


triangles = []
with open("p102_triangles.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        coords = line.split(",")
        tri = [
            (int(coords[0]), int(coords[1])),
            (int(coords[2]), int(coords[3])),
            (int(coords[4]), int(coords[5]))
        ]
        triangles.append(tri)

count = 0
for tri in triangles:
    xd = is_contain_origin(tri)
    # print(tri, xd)
    if xd:
        count += 1
    # print(is_contain_origin(tri))

print(count)
print(f"Time: {time() - start:.12f}")
