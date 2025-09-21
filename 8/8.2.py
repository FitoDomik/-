# ЗАДАНИЕ 8: Комбинаторика
# itertools.permutations/combinations/product
# Перебор всех вариантов строк

from itertools import product

k = 0
for i in product ('0123456', repeat=7) :
    a = ''.join(i)
    if a[0] != '0' and (a.count('0') + a.count('2') + a.count('4')\
    + a.count ('6')) == 2:
        k += 1
print (k)