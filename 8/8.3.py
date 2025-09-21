# ЗАДАНИЕ 8: Комбинаторика
# itertools.permutations/combinations/product
# Перебор всех вариантов строк

from itertools import product

k = 0
for i in product ('0123456789ABCDEF', repeat=3) :
    a = "".join(i)
    if a[0] != '0' and len(set(a)) == len(a):
        a = a. replace ('2' , '0' ) . replace ('4', '0' )\
            .replace ('6', '0') . replace('8', '0') \
            .replace ('A', '0' ) . replace ('C', '0' ) . replace ('E' , '0' )

        a = a. replace ('3', '1' ) . replace ('5', '1' ) \
            .replace ('7', '1') . replace('9', '1') \
            .replace ('B', '1' ) . replace ('D', '1' ) . replace ('F' , '1' )

        if a.count('00') == 0 and a.count('11') == 0:
            k += 1

print(k)