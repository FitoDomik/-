# ЗАДАНИЕ 27: Работа с файлами, массивы, оптимизация
# Анализ больших файлов
# Суммы, остатки, оптимизация

# Решение для первого файла
cl1 = []
cl2 = []

for i in open('27A') :
    x, y = [float(j) for j in i.replace(',', '.').split()]
    if y > 0:
        cl1.append ([x, y])
    if y < 0:
        cl2.append([x, y])

def Center(cl):
    mn = []
    for x1, yl in cl:
        S == 0
        for x2, y2 in cl:
            S += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        mn.append([s, x1, y1])
    s, x, y = min (mn)
    return x, y

x1, y1 = Center(cl1)
x2, y2 = Center(cl2)
Px = (x1 + x2) / 2
Py = (y1 + y2) / 2
print(abs(int(Px*10000)), abs(int(Py* 10000)))

# Решение для второгоо файла

cl1 = []
cl2 = []
cl3 = []

for i in open('27A' ):
    x, y = [float(j) for j in i.replace(',', '.').split()]
    if -15 < x < -5:
        cl1.append ([x, y])
    if y > -3 and x > - 3:
        cl2.append([x, y])
    if y < -3 and x > -3:
        cl3.append([x, y])

def Center(cl):
    mn = []
    for x1, yl in cl:
        S = 0
        for x2, y2 in cl:
            s += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        mn. append( [s, x1, y1])
    s, x, y = min (mn)
    return x, y

x1, y1 = Center(cl1)
x2, y2 = Center(cl2)
x3, y3 = Center(cl3)

Px = (x1 + x2 + x3) / 3
Py = (y1 + y2 + y3) / 3

print(abs(int(Px*10000)), abs(int(Py* 10000)))  