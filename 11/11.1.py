# ЗАДАНИЕ 11: Информационные процессы
# Передача информации, скорость (объем/время)
# Формулы: ceil(log2(alf)), V=dlina*bit/8

from math import*
for x in range(1, 1000):
    alf = 10 + 52 + 500 # символы алфавита
    dlina = x # длина неизвестна
    bit = ceil(log2(alf)) # кодирование алфавита
    V = ceil(dlina * bit / 8) # объем одной детали
    if 45877 * V > 49 * 1024 ** 2:
        print (x)
        break