# ЗАДАНИЕ 25: Перебор делителей
# Проверка числа на делители через цикл
# range(2, int(x**0.5)+1) для эффективного поиска

def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def divs (x):
    d = set ()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted (d)

count = 0
for x in range(7_000_001, 10_000_000) :
    d = [i for i in divs(x) if prime(i)]
    if len(d) > 0:
        M = min(d) + max(d)
        if M % 100 == 13:
            print (x)
            count += 1
        if count > 4:
            break