# ЗАДАНИЕ 15: Логика с условиями
# Решаем через перебор переменных
# all() для проверки всех значений

# Наименьшую длину
otvet = []
for x in range(1, 200):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = False
    F = C <= (((not A) and B) <= (not C))
    if F == 0:
        otvet.append(x)
print(otvet[-1] - otvet[0])

# Наибольшую длину
otvet = []
for x in range(1, 200):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = True
    F = C <= (((not A) and B) <= (not C))
    if F == 1:
        otvet.append(x)
print(otvet[-1] - otvet [0])