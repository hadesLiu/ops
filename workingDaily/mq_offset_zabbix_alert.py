# -*- coding: utf-8 -*-
# author: hiro
import json
import os
import subprocess
import time

'''

1、每两分钟通过日志文件取出 broker port，groupname，offset
2、发送给zabbix server

'''
# 生成json字符串
macros_keys = {"data": []}

topkey = {}
def jsonres(broker_addr, groupname, diff_offset):
    groupname = groupname.strip('[]')
    macros_keys['data'].append({'{#PORT}':broker_addr,"{#GROUPNAME}":groupname})
    topkey["testrocketmq.resource[%s,%s]" % (broker_addr, groupname)] = diff_offset
    #print topkey
    json_queue = json.dumps(macros_keys)
    #send_zabbix_server(json_queue, topkey)
    return json_queue,topkey

# 发送给zabbix server
def send_zabbix_server(json_queue, topkey):

    print "json_queue: %s" % json_queue
    print
    print
    print
    print "topkey: %s" % topkey
    json_res = subprocess.Popen("/usr/local/zabbix/bin/zabbix_sender -z ip_addr -s agent_hostname -k testrocketmq.discovery -o '%s'" % json_queue, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print
    print json_res.stdout.readlines()
    print json_res.stderr.readlines()
    for tp_key,tp_value in topkey.items():
        tp_res = subprocess.Popen("/usr/local/zabbix/bin/zabbix_sender -z ip_addr -s agent_hostname -k '%s' -o '%s'" % (tp_key,tp_value), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print
        print tp_res.stdout.readlines()
        print tp_res.stderr.readlines()

# 读取更新的文件内容
daytime = time.strftime('%Y-%m-%d', time.localtime())
file_path = "/home/rocketmq/9876_4.0/diff-offset-log/"
target_file = file_path + "offset.log-%s" % daytime
file_read_seek = file_path + "file_read_seek.log-%s" % daytime
def log_file():

    print target_file
    if not os.path.exists(file_read_seek):
        fr = open(file_read_seek, "w")
        fr.write("0")
        fr.close()

    with open(target_file, "r") as ft, open(file_read_seek, "r") as fs:
        file_size = int(os.path.getsize(target_file))
        fs_cur_seek = int(fs.read())
        print fs_cur_seek
        if fs_cur_seek < file_size:
            print "updated"
            if fs_cur_seek == 0:
                ft.seek(fs_cur_seek)
            else:
                ft.seek(fs_cur_seek)
            for line in ft.readlines():
                fields = line.split()
                broker_addr = fields[0]
                offset_name = fields[5]
                groupname = fields[6]
                diff_offset = fields[-1]
                if offset_name == "[GROUP_OFFSET]":
                    #print broker_addr, groupname, diff_offset
                    # 拼成json字符串
                    json_queue,topkey = jsonres(broker_addr, groupname, diff_offset)

            file_cur_seek = str(ft.tell())
            with open(file_read_seek, "w") as fs:
                fs.write(file_cur_seek)

            # 发送给 zabbix server
            send_zabbix_server(json_queue, topkey)

        elif fs_cur_seek == file_size:
            print "no update"
        else:
            print "error"

log_file()