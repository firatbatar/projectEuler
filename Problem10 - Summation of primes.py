def isprime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = 2
answer = 0
while n < 2000000:
    if isprime(n):
        answer += n
        n += 1
    else:
        n += 1
print(answer)
