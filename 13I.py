#6.	Определить количество пассажиров, севших в порту Квинстаун,
# в возрастном интервале средний возраст  5 лет и сколько из них выжило
import csv

passangers = []
with open('titanic.csv', newline='') as File:
    all_ages = []
    file = csv.reader(File)
    for i in file:
        try:
            all_ages.append(int(i[5]))
        except:
            continue
        if i[11] == 'Q':
            try:
                passangers.append([int(i[1]), int(i[5])])
            except ValueError:
                continue

average = 0
for i in all_ages:
    average += i
average /= len(all_ages)

answer = 0
answer_alive = 0
for i in passangers:
    if average - 5 < i[1] < average + 5:
        answer += 1
        if i[0] == 1:
            answer_alive += 1

print('Определить количество пассажиров, севших в порту Квинстаун, в возрастном интервале средний возраст  5 лет и сколько из них выжило')
print('количество пассажиров, севших в порту Квинстаун, в возрастном интервале средний возраст  5 лет: ' + str(answer))
print('количество выживших пассажиров , севших в порту Квинстаун, в возрастном интервале средний возраст  5 лет: ' + str(answer_alive))