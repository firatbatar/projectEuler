from time import time
start = time()

mod = 4503599627370517
first_eulercoin = 1504170715041707
modular_inverse = pow(first_eulercoin, -1, mod)
latest_eulercoin = first_eulercoin
total = first_eulercoin
prev = first_eulercoin
switch = False
next_candid = None
max_mult = modular_inverse + 1

while True:
    if switch:
        if next_candid == 15806432:
            break
        # Down to up
        mult = (next_candid * modular_inverse) % mod
        if mult < max_mult:
            max_mult = mult
            total += next_candid
            print(next_candid)
        next_candid += 1

    else:
        # Up to down
        next_candid = (prev + first_eulercoin) % mod
        prev = next_candid
        if next_candid < latest_eulercoin:
            total += next_candid
            latest_eulercoin = next_candid
            print(latest_eulercoin)

        if latest_eulercoin == 15806432:
            switch = True
            next_candid = 1
            print("Switching to down to up search")



print(total)
print(f"Time: {time()-start:.2f}")
