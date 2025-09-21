# ЗАДАНИЕ 13: Двоичные деревья / логика
# Построение дерева вычислений
# ipaddress: ip_network(), маски подсетей

from ipaddress import*

net = ip_network('191.128.66.83/255.192.0.0', 0)
print (net[1]) # наименьший ПК
print (net[-2]) # наибольший ПК