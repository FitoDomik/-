# ЗАДАНИЕ 5: Арифметика в системах счисления
# int('число', base), bin(x), hex(x)
# Перевод: bin(N)[2:], int(binary, 2)

def tr(x) :
    S = ''
    while x > 0:
        S = str(x % 3) + S
        X = x // 3
    return S

otvet = []
for N in range(1, 1000):
    R = tr(N)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R = R + tr(N % 3 * 4)
R = int(R, 3)
if R < 199:
    otvet.append (N)
print(max(otvet))