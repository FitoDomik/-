# ЗАДАНИЕ 17: Числовые последовательности
# Работа с файлами, считывание чисел
# max, min, среднее

a = [int(i) for i in open('17' ) ]
mx_21 = max([i for i in a if abs(i) % 100 == 21 and 9999 < abs(i) <100000] )
otvet = []
for i in range(len(a) - 1):
    if ((abs(a[i]) % 100 == 21 and 9999 < abs(a[i]) < 100000) +
(abs (a[i + 1]) % 100 == 21 and 9999 < abs(a[i + 1]) < 100000)) ==1:

# 6a3a

            if (a[i] ** 2 + a[i + 1] ** 2) >= mx_21 ** 2:
                otvet.append(a[i] + a[i + 1])
print(len(otvet), max(otvet))