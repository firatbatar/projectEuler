def kt():
    answer = 0
    for i in range(1, 101):
        answer += i**2
    return answer


def tk():
    answer = 0
    for i in range(1, 101):
        answer += i
    answer = answer**2
    return answer


a = kt()
b = tk()
print("Kareler Toplamı:", a, sep="")
print("Toplamların Karesi:", b, sep="")
sonuc = abs(a-b)
print("Farkları:", sonuc, sep="")
