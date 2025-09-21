# ЗАДАНИЕ 25: Перебор делителей
# Проверка числа на делители через цикл
# range(2, int(x**0.5)+1) для эффективного поиска

def D(x) :
    dels = set ()
    for d in range(2, int(x ** 0.5) +1):
        if x % d == 0:
            dels.add(d)
            dels.add(x // d)
    return dels

k = 0
for x in range(800001, 10 ** 10):
    dels = D(x)
    dels9 = [i for i in dels if i % 10 == 9 and i != 9]
    if len(dels9) > 0:
        print(x, min(dels9))
        k += 1
    if k == 5:
        break