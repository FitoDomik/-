# ЗАДАНИЯ 19-21: Файлы, массивы
# with open("file.txt") as f: data = list(map(int, f))
# Задачи на обработку числовых последовательностей

# 19 - с неудачным ходом
def F(k1, k2, x):
    if x == 3 and (k1 + k2) >= 123:
        return True
    if x == 3 and (k1 + k2) < 123:
        return False
    if (k1 + k2) >= 123:
        return False
    if x % 2 == 0:
        return (F(k1 + 1, k2, x + 1) or F(k1* 2, k2, x + 1) or F(k1, k2 +1,x+1) or F(k1, k2*2,x+1))
    else :
        return (F(k1 + 1, k2, x + 1) or F(k1 * 2, k2, x +1) or F(k1, k2+1,x+1) or F(k1, k2*2,x+1))

for k2 in range(1, 110):
    if F(13, k2, 1):
        print(k2)

# 20

def F(k1, k2, x) :
    if x == 4 and (k1 + k2) >= 123:
         return True
    if x == 4 and (k1 + k2) < 123:
     return False
    if (k1 + k2) >= 123:
        return False
    if x % 2 == 1:
        return (F(k1 + 1, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2 +1, x+1) or F(k1, k2*2,x+1))
    else :
        return (F(k1 + 1, k2, x + 1) and F(k1 * 2, k2, x +1) and F(k1, k2 + 1, x+1) and F(k1, k2*2,x+1))

for k2 in range(1, 110):
    if F(13, k2, 1):
        print(k2)

# 21

def F(k1, k2, x) :
    if (x == 3 or x == 5) and (k1 + k2) >= 123:
        return True
    if x == 5 and (k1 + k2) < 123:
        return False
    if (k1 + k2) >= 123:
        return False
    if x % 2 == 0:
        return (F(k1 + 1, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2 +1, x+1) or F(k1, k2*2, x+1))
    else :
        return (F(k1 + 1, k2, x + 1) and F(k1 * 2, k2, x + 1) and F(k1, k2 + 1, x+1) and F(k1, k2*2,x+1))

for k2 in range(1, 110):
    if F(13, k2, 1):
        print(k2)