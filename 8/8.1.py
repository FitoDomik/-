# ЗАДАНИЕ 8: Комбинаторика
# itertools.permutations/combinations/product
# Перебор всех вариантов строк

from itertools import product

alf = sorted ( 'ПАРУС' )
nomer = 0
for i in product(alf, repeat=5):
    slovo = ''.join(i)
    nomer += 1
    if slovo. count ('y') <= 1 and slovo.count ('AA') == 0:
        print (nomer)