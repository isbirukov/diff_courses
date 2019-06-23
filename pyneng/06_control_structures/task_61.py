"""
Запросить у пользователя ввод IP-адреса в формате 10.0.1.1.
Определить какому классу принадлежит IP-адрес.
В зависимости от класса адреса, вывести на стандартный поток вывода:
'unicast' - если IP-адрес принадлежит классу A, B или C
'multicast' - если IP-адрес принадлежит классу D
'local broadcast' - если IP-адрес равен 255.255.255.255
'unassigned' - если IP-адрес равен 0.0.0.0
'unused' - во всех остальных случаях
Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239
"""

ip = input("Enter ip: ")
ip = ip.strip().split(".")

# trasform 'str' in list into 'int'
ip = list(map(int, ip))

if (1 <= ip[0] <= 223):
	print('unicast')
elif (224 <= ip[0] <= 239):
	print('multicast')
elif (ip[0] == 255) and (ip[1] == 255) and (ip[2] == 255) and (ip[3] == 255):
	print('local broadcast')
elif (ip[0] == 0) and (ip[1] == 0) and (ip[2] == 0) and (ip[3] == 0):
	print('unassigned')
else:
	print('unused')
