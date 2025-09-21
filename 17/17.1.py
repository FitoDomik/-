# ЗАДАНИЕ 17: Числовые последовательности
# Работа с файлами, считывание чисел
# max, min, среднее

a = [int(i) for i in open('17.txt' )]
mx_19 = max([i for i in a if i % 19 == 0] )
otvet = []
for i in range(len(a) - 1):
    if ((a[i] >mx_19) + (a[i+1]>mx_19)) > 0:
        otvet.append(a[i] + a[i +1])
print(len(otvet), max(otvet))