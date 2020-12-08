# 2. What is CIDR in IP Notation? Write a Program to accept the IP in CIDR from user and accept
# another plain IP and check the IP is matched with earlier IP in CIDR.
# E.g.
#            1. First IP in CIDR: 172.16.16.142/24
#            Second plain IP: 172.16.16.89
#             Result should be matched
#            2. First IP in CIDR: 172.16.16.142/24
#            Second plain IP: 172.16.1.47
#             Result should be not matched

from ipaddress import IPv4Address
from ipaddress import IPv4Network


IP_in_CIDR = IPv4Network(input('Enter the IP in CIDR :'), False)
Plain_IP = IPv4Address(input('Enter the Plain IP :'))
if Plain_IP in IP_in_CIDR:
    print("Matched")
else:
    print('Not matched')
