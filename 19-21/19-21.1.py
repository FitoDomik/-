# ЗАДАНИЯ 19-21: Файлы, массивы
# with open("file.txt") as f: data = list(map(int, f))
# Задачи на обработку числовых последовательностей

# 19
def F(k, x) :
    if x == 3 and k >= 435:
        return True
    if x == 3 and k < 435:
        return False
    if k >= 435:
        return False
    if x % 2 == 0:
        return F(k + 5, x + 1) or F(k * 3, x +1)
    else:
        return F(k + 5, x + 1) and F(k * 3, x + 1)

for k in range(1, 435):
    if F(k, 1):
        print (k)

# 20
def F(k, x) :
    if x == 4 and k >= 435:
        return True
    if x == 4 and k < 435:
        return False
    if k > 435:
        return False
    if x % 2 == 1:
        return F(k + 5, x + 1) or F(k * 3, x + 1)
    else:
        return F(k + 5, x + 1) and F(k * 3, x + 1)

for k in range(1, 435):
    if F(k, 1):
        print(k)

# 21
def F(k, x) :
    if (x == 3 or x == 5) and k >= 435:
        return True
    if x == 5 and k < 435:
        return False
    if k >= 435:
        return False
    if x % 2 == 0:
        return F(k + 5, x + 1) or F(k * 3, x +1)
    else:
        return F(k + 5, x + 1) and F(k * 3, x +1)

for k in range(1, 435):
    if F(k, 1):
        print (k)
# не учитываем значения из 19 номера, если при любой игре Пети