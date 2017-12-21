# -*- coding:utf-8 -*-
# author: hiro
import os
import pycurl as pycurl

import sys

'''
getinfo(option)方法，对应libcurl包中的curl_easy_get-info方法，
参数option是通过libcurl的常量来指定的。
下面列举常用的常量列表：
c = pycurl.Curl ()    #创建一个curl对象
c.getinfo (pycurl.HTTP_CODE)    #返回的HTTP状态码
c.getinfo (pycurl.TOTAL_TIME)    #传输结束所消耗的总时间
c.getinfo (pycurl.NAMELOOKUP_TIME)    #DNS解析所消耗的时间
c.getinfo (pycurl.CONNECT_TIME)    #建立连接所消耗的时间
c.getinfo (pycurl.PRETRANSFER_TIME)    #从建立连接到准备传输所消耗的时间
c.getinfo (pycurl.STARTTRANSFER_TIME)    #从建立连接到传输
'''

# 示例：实现探测Web服务质量

# URL = "http://www.google.com.hk"  #探测的目标URL
URL = "http://interface.mamayz.com/stationin/post"  #探测的目标URL

c = pycurl.Curl()

c.setopt(pycurl.URL, URL)
c.setopt(pycurl.CONNECTTIMEOUT, 5)
c.setopt(pycurl.TIMEOUT, 5)
c.setopt(pycurl.NOPROGRESS, 1)
c.setopt(pycurl.FORBID_REUSE, 1)
c.setopt(pycurl.MAXREDIRS, 1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)

indexfile = open(os.path.dirname(os.path.realpath(__file__))+
                 "/context.txt", 'wb')
c.setopt(pycurl.WRITEHEADER, indexfile)
try:
    c.perform()
except Exception, e:
    print "connection error: " + str(e)
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print ""
print "HTTP状态码： %s" % (HTTP_CODE)
print "DNS解析时间： %s" % (NAMELOOKUP_TIME)
print "建立连接时间:%.2f ms" % (CONNECT_TIME*1000)
print "准备传输时间:%.2f ms" % (PRETRANSFER_TIME*1000)
print "传输开始时间:%.2f ms" % (STARTTRANSFER_TIME*1000)
print "传输结束总时间:%.2f ms" % (TOTAL_TIME*1000)
print "下载数据包大小:%d bytes/s" % (SIZE_DOWNLOAD)
print "HTTP头部大小:%d byte" % (HEADER_SIZE)
print "平均下载速度:%d bytes/s" % (SPEED_DOWNLOAD)

indexfile.close()
c.close()
