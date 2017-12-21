# -*- coding:utf-8 -*-
# author: hiro

# simple
import difflib

# 定义字符串1
# text1 = """text1:
# This module provides classes and functions for comparing sequences.
# including HTML and context and unified diffs.difflib document v7.4
# add string"""
# 以行进行分隔，以便进行对比
# text1_lines = text1.splitlines()

# 定义字符串2
# text2 = """text2:
# This module provides classes and functions for Comparing sequences.
# including HTML and context and unified diffs.difflib document v7.5"""
# text2_lines = text2.splitlines()

# 创建Diff() 对象
# d = difflib.Differ()
# # 采用compare方法对字符串进行比较
# diff = d.compare(text1_lines, text2_lines)
# print '\n'.join(list(diff))

# 创建 HtmlDiff() 对象
# d = difflib.HtmlDiff()
# print d.make_file(text1_lines, text2_lines)

# compare nginx config file
import sys
try:
    textfile1 = sys.argv[1]  # 第一个配置文件路径参数
    textfile2 = sys.argv[2]  # 第二个配置文件路径参数
except Exception as e:
    print "Error: " + str(e)
    print "Usage: basic2.1_difflib_file.py filename1 filename2"
    sys.exit()

def readfile(filename): # 文件读取分隔函数
    try:
        fileHandle = open(filename, 'rb')
        # 读取后 以行进行分割
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except Exception as e:
        print ('Read file Error: ' + str(error))
        sys.exit()
if textfile1 == "" or textfile2 == "":
    print "Usage: basic2.1_difflib_file.py filename1 filename2"
    sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)

