# ЗАДАНИЕ 8: Комбинаторика
# itertools.permutations/combinations/product
# Перебор всех вариантов строк

from itertools import product

k = 0
for i in product ('01234567', repeat=5) :
    a = ''.join (i)
    if a[0] in '2468' and a[-1] not in '26' and a. count('7') <= 2:
        k += 1
print(k)