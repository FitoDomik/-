# ЗАДАНИЕ 13: Двоичные деревья / логика
# Построение дерева вычислений
# ipaddress: ip_network(), f'{ip:b}' для двоичного представления

from ipaddress import*

k = 0
for ip in ip_network('112.208.0.0/255.255.128.0', 0):
    ip_2 = f'{ip:b}' # wnn bin(int(ip) [2:]).zfill(32)
    if ip_2.count ('1') % 11 == 0:
        k += 1

print (k)