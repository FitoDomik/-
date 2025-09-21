# ЗАДАНИЕ 5: Арифметика в системах счисления
# int('число', base), bin(x), hex(x)
# Перевод: bin(N)[2:], int(binary, 2)

def DVOICHKA(x):
    if x == 0:
        return '0'
    S = ''
    while x > 0:
        S = str(x % 2) + S
        X = x // 2
    return S

otvet = []
for N in range(1, 1000):
    R = DVOICHKA(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += DVOICHKA(N % 3 * 3)
    R = int(R, 2)
    if R > 195:
        otvet.append (R)

print(min(otvet))