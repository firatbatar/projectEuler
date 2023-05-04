months_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days_names = {1: "Pazartesi", 2: "Salı", 3: "Çarşamba", 4: "Perşembe", 5: "Cuma", 6: "Cumartesi", 7: "Pazar"}
day = 2
year = 1901
answer = 0

while year != 2001:
    for i in months_days:
        for n in range(1, months_days[i]+1):
            day += 1
            if day == 8:
                day = 1
            if day == 7:
                if n == 1:
                    answer += 1
    year += 1
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                months_days[2] = 29
        else:
            months_days[2] = 29
    else:
        months_days[2] = 29
print(answer)