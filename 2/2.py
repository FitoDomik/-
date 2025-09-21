# ЗАДАНИЕ 2: Логические выражения
# ¬ not, ∧ and, ∨ or, → => (эквивалент: (not A) or B), ≡ ==
# Таблицы истинности: itertools.product([0,1], repeat=n)
# 1) ¬ not
# 2) ∧ and
# 3) ∨ or
# 4) → =>
# 5) ≡ ==

from itertools import*

def F(x, y, z, w) :
    return ((w <= y) <= x) or (not z)

for al, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7) :
    table = [(al, a2, 1, a3), (a4, 0, a5, a6),(a7,1,0,0)]
    if len(set(table)) == len(table):
        for i in permutations ('xyzw' ) :
            if [F( ** dict(zip(i, r))) for r in table] == [0,0,0]:
                print(*i, sep='')
