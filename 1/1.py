# ЗАДАНИЕ 1: Системы счисления
# bin(), oct(), hex(), int(x, base)
# 2→двоичная, 8→восьмеричная, 16→шестнадцатеричная
# Перевод: int('1010', 2) → 10

from itertools import permutations

table = '14 15 17 24 26 35 36 37 41 42 51 53 56 62 63 65 71 73'
graph = 'AB BA AC CA EC CE CG GC EF FE FG GF FD DF DG GD DB BD'

for per in permutations ( 'ABCDEFG' ) :
    new_table = table
    for i in range(1, 7 + 1):
        new_table = new_table. replace(str(i), per[i - 1])
if set(new_table.split()) == set(graph.split()):
    print('1 2 3 4 5 6 7')
    print (*per)
#1 2 3 4 5 6 7
# CBFA G DE