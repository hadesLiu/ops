#!/usr/bin/evn python
#-*-coding:utf-8 -*-
import time
import logging,warnings
import subprocess

from scapy.all import traceroute
warnings.filterwarnings("ignore",category=DeprecationWarning)
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
domains = raw_input('Please input domains or IPs: ')

try:
    domain = domains.split(' ')
    res,unans = traceroute(domain,dport=[80,443],retry=-2)
    res.graph(target=">test.svg")
    time.sleep(1)
    subprocess.Popen("/usr/bin/convert test.svg test.png", shell=True)
except:
    print "you shoud run by root or domain error"
