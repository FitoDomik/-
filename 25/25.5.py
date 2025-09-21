# ЗАДАНИЕ 25: Перебор делителей
# Проверка числа на делители через цикл
# range(2, int(x**0.5)+1) для эффективного поиска

def D(x):
    dels = set ()
    for d in range(2, int(x ** 0.5) +1):
        if x % d == 0:
            dels.add(d)
            dels.add(x // d)
    return dels

k = 0
for x in range(500001, 10 ** 10):
    dels = D(x)
    if len(dels) > 0:
        R = sum(dels)
        if R % 10 == 9:
            print(x, R)
            k += 1
        if k == 5:
            break