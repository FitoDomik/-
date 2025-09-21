# ЗАДАНИЕ 17: Числовые последовательности
# Работа с файлами, считывание чисел
# max, min, среднее

a = [int(i) for i in open('17.txt' )]
mx3 = max([j for j in a if abs(j) % 10 == 3 and 99 < abs(j) <1000] )
o = []
for i in range(len(a) - 2):
    s = a[i:i + 3]
    if len([j for j in s if abs(j) % 10 == 3 and 99 < abs(j) <1000]) > 0:
        if sum(s) < mx3:
            o. append (sum(s))
print(len(o), max(o))