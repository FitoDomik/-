# ЗАДАНИЕ 15: Логика с условиями
# Решаем через перебор переменных
# all() для проверки всех значений

def F(A, x, y) :
    return (x + 2*y > A) or (y < x) or (x < 30)
for A in range(0, 1000):
    if all(F(A, x, y) for x in range(0, 1000)\
    for y in range(0, 1000)):
        print (A)