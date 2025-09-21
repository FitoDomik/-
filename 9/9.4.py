# ЗАДАНИЕ 9: Тексты и строки
# text.count("ABC"), text.replace()
# Работа с файлами: open(), split()

n = 0
for i in open('9') :
    a = [int(j) for j in i.split()]
    n += 1
    pov_2 = [j for j in a if a.count(j) == 2]
    pov_1 = [j for j in a if a.count(j) == 1]
    if len(pov_2) == 2 and len(pov_1) == 4:
        if pov_2[0] >= sum(pov_1) / len(pov_1):
            print (n)
            break