from time import time
start = time()


def find_numbers(keylog):
    numbers = set()
    for attempt in keylog:
        for num in attempt:
            numbers.add(num)
    return numbers


def connections(attempt):
    l = len(attempt)
    for i in range(l - 1):
        for j in range(i + 1, l):
            yield attempt[i], attempt[j]


def make_number_graph(keylog):
    graph = dict()
    for attempt in keylog:
        for a, b in connections(attempt):
            if a not in graph:
                graph[a] = {b}
            else:
                graph[a].add(b)
    return graph


with open('../txt/p079_keylog.txt', 'r') as file:
    keylog = file.read().split('\n')

numbers = find_numbers(keylog)
graph = make_number_graph(keylog)
b = dict()


for num in numbers:
    for val in graph.values():
        if num in val:
            if num not in b:
                b[num] = 1
            else:
                b[num] += 1
    if num not in b:
        b[num] = 0

answer = ""
# print(graph)
# print(b)
while b:
    biggestK = None
    biggestV = -1
    for k, v in b.items():
        if v > biggestV:
            biggestK = k
            biggestV = v
    temp = answer
    answer = str(biggestK)
    answer += temp
    b.pop(biggestK)


print(answer)
print(f"Time: {time()-start:.3f}")
