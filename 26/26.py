# ЗАДАНИЕ 26: Оптимизация выбора (рюкзак)
# Жадный алгоритм или динамика
# Сортировка и выбор оптимального решения

f = open('26')
n = int (f.readline ())
a = []
n = 0

for i in f:
    x, y = [int(x) for x in i.split()]
    n += 1
    if x < y:
        a. append ( [x, n,
            ' срок его хранения с момента изготовления'])
    else:
        a. append ( [x, n,
            'срок годности к употреблению после вскрытия продукта'])


a. sort ()
otvet1 = a[ -1] [1]
lenta = [0] * (n + 1)
l= 0
r = 0

for i in a:
    if i[2] == 'срок его храннеия с момента изготовления':
        lenta[l] = i[1]
        l += 1
    else:
        lenta[r] = i[1]
        r -= 1

k = 0
for i in range(len(lenta)):
    if lenta[i] == otvet1:
        k = len(lenta [i+1:] )
        break

print(otvet1, k)