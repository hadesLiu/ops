# -*- coding:utf-8 -*-
# author: hiro

# PortScanner class usage
from nmap import nmap

nm = nmap.PortScanner()
print nm.scan("172.16.100.70", '22, 80')

print nm.command_line()
print nm.scaninfo()