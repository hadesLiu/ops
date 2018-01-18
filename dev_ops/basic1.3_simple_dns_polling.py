# -*- coding:utf-8 -*-
# author: hiro
import httplib

import dns.resolver

iplist = [] # 定义域名IP列表变量
# appdomain = "www.google.com.hk" # 定义业务域名
appdomain = "www.dianwoda.com" # 定义业务域名

def get_iplist(domain=""): #域名解析函数，解析成功IP将被追加到iplist
    try:
        A = dns.resolver.query(domain, 'A') #解析Ａ记录
    except Exception as e:
        print 'dns resovler error: ' + str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address) # 追加到iplist
    return True

def checkip(ip):
    checkurl = ip + ':80'
    getcontent = ''
    httplib.socket.setdefaulttimeout(5) # 定义http连接超时时间5秒
    conn = httplib.HTTPConnection(checkurl) # 创建http连接对象

    try:
        # 发起URL请求，添加host主机头
        conn.request("GET", "/", headers={"Host":appdomain})

        r = conn.getresponse()
        getcontent = r.read(15) # 获取URL页前面15个字符，以便做可用性校验
    finally:
        # 监控URL页的内容一般是事先定义好的，比如 "HTTP 200" 等
        if getcontent == "<!doctype html>":
            print ip + "[OK]"
        else:
            # 此处可放告警程序，可以是邮件/短信通知
            print ip + "[Error]"

# if __name__ == "__main__":
#     # 条件：域名解析正确且至少返回一个IP
#     if get_iplist(appdomain) and len(iplist) > 0:
#         for ip in iplist:
#             checkip(ip)
#     else:
#         print "dns resolver error."

if get_iplist(appdomain) and len(iplist) > 0:
    for ip in iplist:
        checkip(ip)
else:
    print "dns resolver error."




