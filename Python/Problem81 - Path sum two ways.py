from time import time
start = time()


def find_min(data):
    for i in range(0, len(data))[::-1]:
        for j in range(0, len(data[i]))[::-1]:
            try:
                data[i][j] += min(data[i][j + 1], data[i + 1][j])
            except IndexError:
                try:
                    data[i][j] += data[i][j + 1]
                except IndexError:
                    try:
                        data[i][j] += data[i + 1][j]
                    except IndexError:
                        continue
    return data[0][0]


def create_2D_array(size):
    array = []
    for i in range(size):
        array.append([])
    return array


# with open('p081-2-3_test.txt', 'r') as file:
#     size = 5
#     matrix = create_2D_array(size)
#     xd = file.read().split('\n')
#     rows = []
#     for i in xd:
#         rows.append(i.split(','))
#     # print(rows)
#     for i in range(0, size):
#         for row in rows:
#             matrix[i].append(int(row[i]))


with open('../txt/p081_matrix.txt', 'r') as file:
    size = 80
    matrix = create_2D_array(size)
    xd = file.read().split('\n')
    rows = []
    for i in xd:
        rows.append(i.split(','))
    # print(rows)
    for i in range(0, size):
        for row in rows:
            matrix[i].append(int(row[i]))


# print(matrix)
print(find_min(matrix))
print(f"Time: {time() - start:.2f}")