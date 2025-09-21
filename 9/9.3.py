# ЗАДАНИЕ 9: Тексты и строки
# text.count("ABC"), text.replace()
# Работа с файлами: open(), split()

for i in open('9'):
    a = [int(j) for j in i.split()]
    pov_2 = [j for j in a if a. count(j) == 2]
    pov_1 = [j for j in a if a.count(j) == 1]
    if len(pov_2) == 4 and len(pov_1) == 3:
        if max(a) not in pov_2:
            print (sum(a))
            break