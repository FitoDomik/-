def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return x > 1

k = 0
for x in range(2_900_000, 5_000_000):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    
    b = list(d)
    if (len(d) == 2 and str(b[0]).count('0') == 1 and
        str(b[1]).count('0') == 1 and b[0] * b[1] == x and
        prime(b[0]) and prime(b[1])):
        print(x, max(b))
        k += 1
        if k == 5:
            break