# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace(',', '')
ospf_route = ospf_route.strip().split()
ospf_route[2] = ospf_route[2].strip('[]')
ospf_route.pop(0)
ospf_route.pop(2)

print("""Protocol:{:>18}
Prefix:{:>28}
AD/Metric:{:>19}
Next-Hop:{:>23}
Last update:{:>16}
Outbound Interface{:>20}""".format('OSPF', ospf_route[0], ospf_route[1], ospf_route[2], ospf_route[3], ospf_route[4]))
