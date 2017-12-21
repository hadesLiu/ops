# -*- coding:utf-8 -*-
# author: hiro
import filecmp

# 单文件对比

# print filecmp.cmp("/home/hiro/PycharmProjects/ops/nginx.conf.v1", "/home/hiro/PycharmProjects/ops/nginx.conf.v3")
# print filecmp.cmp("/home/hiro/PycharmProjects/ops/nginx.conf.v1", "/home/hiro/PycharmProjects/ops/nginx.conf.v3")

# 多文件对比

# dir2
# md5sum *
# d9dfc198c249bb4ac341198a752b9458  f1
# aa9aa0cac0ffc655ce9232e720bf1b9f  f2
# 33d2119b71f717ef4b981e9364530a39  f3
# d9dfc198c249bb4ac341198a752b9458  f5
# dir1
# md5sum *
# d9dfc198c249bb4ac341198a752b9458  f1
# aa9aa0cac0ffc655ce9232e720bf1b9f  f2
# d9dfc198c249bb4ac341198a752b9458  f3
# 410d6a485bcf5d2d2d223f2ada9b9c52  f4
#
# >>>filecmp.cmpfiles ("/home/test/filecmp/dir1",
# "/home/test/filecmp/dir2",
# ['f1', 'f2', 'f3', 'f4', 'f5'])
#
# (['f1', 'f2'], ['f3'], ['f4', 'f5'])

# 目录对比  dircmp



