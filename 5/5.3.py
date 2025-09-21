# ЗАДАНИЕ 5: Арифметика в системах счисления
# int('число', base), bin(x), hex(x)
# Перевод: bin(N)[2:], int(binary, 2)

def dv(x) :
    S = ''
    while x > 0:
        S = str(x % 2) + S
        X = x // 2
    return S

otvet = []
for N in range(1, 1000):
    R = dv (N)
    sm = sum(map(int, R) )
    if sm % 2 == 0:
        R = '10' + R[2 : ] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int (R, 2)
    if R > 50:
        otvet.append (N)
print(min(otvet))