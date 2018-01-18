# -*- coding:utf-8 -*-
# author: hiro

import dns.resolver

# A 记录

domain = raw_input("Please input a domain: ")
A = dns.resolver.query(domain, 'A')

for i in A.response.answer:
    print "i: %s" % i
    for j in i.items:
        print "j: %s" % j
        print j.address

# MX 记录

# domain = raw_input("Please input an domain: ")
# MX = dns.resolver.query(domain, 'MX')
# for i in MX:
#     print i
#     print 'MX prefrence = ', i.preference
#     print 'mail exchanger = ', i.exchange

# NS 记录

# domain = raw_input('Please input an domain：')
# ns = dns.resolver.query(domain, 'NS')
# for i in ns.response.answer:
#     for j in i.items:
#         print j.to_text()

# CNAME 记录
# assets.dianwoda.cn

# domain = raw_input('Please input an domain：')
# cname = dns.resolver.query(domain, 'CNAME')
# for i in cname.response.answer:
#     for j in i.items:
#         print j.to_text()

