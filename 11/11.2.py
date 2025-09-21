# ЗАДАНИЕ 11: Информационные процессы
# Передача информации, скорость (объем/время)
# Формулы: ceil(log2(alf)), V=dlina*bit/8

from math import*

for x in range(1, 1000) :
    alf = x
    dlina = 172
    bit = ceil(log2(alf))
    V = ceil(dlina * bit / 8)
    if 356984 * V >= 54 * 1024 ** 2:
        print (x)
        break