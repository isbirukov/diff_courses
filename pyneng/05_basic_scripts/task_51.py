"""Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:
Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000 """


input_str = input("Enter ip address: ")
#ip = ip.strip().split('.')
sep_ind = input_str.find('/')
ip = input_str[:sep_ind]
ip = ip.strip().split('.')

mask = input_str[sep_ind+1:]
print(ip)
print(mask)
str1 = """
Network:
{:8} {:8} {:8} {:8}
{:0>8b} {:0>8b} {:0>8b} {:0>8b}
"""
print(str1.format(ip[0], ip[1], ip[2], ip[3], int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))