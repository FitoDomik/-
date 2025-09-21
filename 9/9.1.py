# ЗАДАНИЕ 9: Тексты и строки
# text.count("ABC"), text.replace()
# Работа с файлами: open(), split()

k = 0
for i in open ('9') :
    a = [int(j) for j in i.split()]
    pov_1 = sorted([j for j in a if a.count(j) == 1])
    pov_2 = [j for j in a if a. count(j) == 2]
    if len(pov_2) == 2 and len(pov_1) == 5:
        if (pov_1[0] * pov_1[1] * pov_1[2]) > pov_2[0] ** 2:
            k += 1
print (k)