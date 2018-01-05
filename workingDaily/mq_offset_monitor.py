# -*- coding:utf-8 -*-
# author: hiro
# -*- coding: utf-8 -*-
# author: hiro

import subprocess
import re
import json,time
import sys,socket
import datetime

def broker_topic_consumergroup():
    brokerAddrs = ["172.24.0.11:10711","172.24.0.12:10711","172.24.0.13:10711","172.24.0.14:10711","172.24.1.3:10711","172.24.1.4:10711"]
    for brok in brokerAddrs:
        items = subprocess.Popen("bash /home/rocketmq/29876_4.0/apache-rocketmq-all/bin/mqadmin brokerConsumeStats -n 127.0.0.1:29876 -b %s" % brok,
                                 shell=True, env={"JAVA_HOME":"/usr/local/jdk"}, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        consumers = {}
        brokers = {}
        topic = {}

        items.stdout.readline() # 去除首行
        for line in items.stdout.readlines():
            try:
                line = line[:-1]
                if not line: continue
            except:
                continue

            try:
                fields = line.split()
                fields[7] = fields[7] + " " + fields[8] # 最后一列时间特殊处理
                del fields[8]

                broker_name = fields[2]
                topic_name = fields[0]
                consumer_group = fields[1]
                diff_offset = fields[6]

                # broker 总的diffset
                if brokers.get(broker_name, -1) == -1:
                    brokers[broker_name] = int(diff_offset)
                else:
                    pre_diff = brokers.get(broker_name, 0)
                    cur_diff = pre_diff + int(diff_offset)
                    brokers[broker_name] = cur_diff

                # topic_offset_relation
                if topic.get(topic_name, -1) == -1:
                    topic[topic_name] = int(diff_offset)
                else:
                    pre_diff = topic.get(topic_name, 0)
                    cur_diff = pre_diff + int(diff_offset)
                    topic[topic_name] = cur_diff

                # topic 和 consumerGroup 组成的key, diffoffset 值
                consumer_name = topic_name+"@"+consumer_group
                if consumers.get(consumer_name, -1) == -1:
                    consumers[consumer_name] = int(diff_offset)
                else:
                    pre_diff = consumers.get(consumer_name, 0)
                    cur_diff = pre_diff + int(diff_offset)
                    consumers[consumer_name] = cur_diff

            except:
                continue
            #print fields

        cur_time = datetime.datetime.now()
        cur_time = datetime.datetime.strftime(cur_time, "%Y-%m-%d %H:%M:%S")
        all_broker_diff_offset = []
        all_topic_diff_offset = []
        all_consumer_diff_offset = []
        log_date = datetime.datetime.now().date()
        log_date = datetime.datetime.strftime(log_date, "%Y-%m-%d")
        offset_log_name = "/home/rocketmq/diff-offset-log/offset.log-%s" % log_date

        with open(offset_log_name, "a") as f:
            '''
            拼接 broker 和 diff offset
            broker:
            ip:port/brokername 2018-01-02 14:02:00 INFO - [BROKER_OFFSET] [brokername] Stats In One Minute, DIF: 0
            '''
            for broker_name in brokers:
                broker_diff_offset = "%s %s INFO - [BROKER_OFFSET] [%s] Stats In One Minute, DIFF: %s" % (brok, cur_time, broker_name, brokers[broker_name] )
                all_broker_diff_offset.append(broker_diff_offset)
            for index in range(len(all_broker_diff_offset)):
                f.write(all_broker_diff_offset[index] + "\n")

            '''
            拼接 topic 和 diff offset
            topic:
            ip:port/brokername 2018-01-02 14:02:00 INFO - [TOPIC_OFFSET] [TopicName] Stats In One Minute, DIF: 0
            '''
            for topic_name in topic:
                topic_diff_offset =  "%s %s INFO - [TOPIC_OFFSET] [%s] Stats In One Minute, DIFF: %s" % (brok, cur_time, topic_name, topic[topic_name])
                all_topic_diff_offset.append(topic_diff_offset)
            for index in range(len(all_topic_diff_offset)):
                f.write(all_topic_diff_offset[index] + "\n")

            '''
            拼接 consumer 和 diff offset
            group:
            ip:port/brokername 2018-01-02 14:02:00 INFO - [GROUP_OFFSET] [TopicName@groupName] Stats In One Minute, DIF: 0
            '''
            for consumer_name in consumers:
                consumer_diff_offset =  "%s %s INFO - [GROUP_OFFSET] [%s] Stats In One Minute, DIFF: %s" % (brok, cur_time, consumer_name, consumers[consumer_name])
                all_consumer_diff_offset.append(consumer_diff_offset)
            for index2 in range(len(all_consumer_diff_offset)):
                f.write(all_consumer_diff_offset[index2] + "\n")

broker_topic_consumergroup()