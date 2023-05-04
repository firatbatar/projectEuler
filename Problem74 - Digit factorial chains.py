from time import time
from math import factorial as f
start = time()


def create_next(num):
    strNum = str(num)
    new = 0
    for i in strNum:
        new += f(int(i))
    return new


def create_chain(num, chains):
    chain = []
    next = num
    while True:
        if next in chains:
            return len(chain) + chains[next]
        if next not in chain:
            chain.append(next)
            next = create_next(next)
        else:
            break
    return len(chain)


# notOk = []
chains = {}
oks = []
for n in range(1, 10**6):
    chain_len = create_chain(n, chains)
    if chain_len == 60:
        oks.append(n)
    chains[n] = chain_len
print(len(oks))
print(f"Time: {time() - start:.3f}")
