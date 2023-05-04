def self_power(last):
    num = 0
    for n in range(1, last+1):
        num += n**n
    return str(num)


number = self_power(1000)
print(number[-10:])
