# -×- coding:utf-8 -*-

# IP address

from IPy import IP

# ip = IP('10.0.0.0/8')
# ip = IP('::1')
# ip = IP('192.168.0.0/16')
# print ip.version()
# print ip.len()
#
# for x in ip:
#     print x

# ip = IP('192.168.1.20')
# print ip.reverseName()
# print ip.iptype()
# print IP('8.8.8.8').iptype()
# print IP('8.8.8.8').int()
# print IP('8.8.8.8').strHex()
# print IP('8.8.8.8').strBin()
# print IP(0x8080808)

# print IP('192.168.1.0').make_net('255.255.255.0')
# print IP('192.168.1.0/255.255.255.0', make_net=True)
# print IP('192.168.1.0-192.168.1.255', make_net=True)
#
# print IP('192.168.1.0/24').strNormal(0)
# print IP('192.168.1.0/24').strNormal(1)
# print IP('192.168.1.0/24').strNormal(2)
# print IP('192.168.1.0/24').strNormal(3)

# Multiple IP address Relationship

# print IP('10.0.0.0/24') < IP('12.0.0.0/24')
# print '192.168.1.100' in IP('192.168.1.0/24')
# print IP('192.168.1.0/24') in IP('192.168.0.0/16')
# print IP('192.168.0.0/23').overlaps('192.168.1.0/24')
# print IP('192.168.1.0/24').overlaps('192.168.2.0')

# 示例　根据输入的IP或子网返回网络、掩码、广播、反向解析、子网数、IP类型等信息。

ip_s = raw_input('Please input an IP or net-range: ')
ips = IP(ip_s)
if len(ips) > 1:
    print 'net: %s' % ips.net()
    print 'netmask: %s' % ips.netmask()
    print 'broadcast: %s' % ips.broadcast()
    print 'reverse address: %s' % ips.reverseNames()
    print 'subnet: %s' % len(ips)
else:
    print 'reverse address: %s' % ips.reverseNames()[0]
    print 'hexadecimal: %s' % ips.strHex()
    print 'binary ip: %s' % ips.strBin()
    print 'iptype: %s' % ips.iptype()




# 参考资料
# https://sourcecodebrowser.com/ipy/0.62/class_i_py_1_1_i_pint.html

