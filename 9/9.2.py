# ЗАДАНИЕ 9: Тексты и строки
# text.count("ABC"), text.replace()
# Работа с файлами: open(), split()

k = 0
for i in open('17'):
    a = sorted([int(j) for j in i.split()])
    if a[3] < (a[0] + a[1] + a[2]):
        if (a[3] + a[0]) == (a[1] + a[2]):
            k += 1
print (k)