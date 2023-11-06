answer = 1
for i in range(3, 1002, 2):
    sag_ust_kose = i**2
    sol_ust_kose = (sag_ust_kose-(i-1))
    sol_alt_kose = (sol_ust_kose-(i-1))
    sag_alt_kose = (sol_alt_kose-(i-1))
    answer += sag_ust_kose
    answer += sol_alt_kose
    answer += sol_ust_kose
    answer += sag_alt_kose
print(answer)
