#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-16 22:46
# @Author  : hys
# @Site    : 
# @File    : alice.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com
file_name = "alice_test.txt"
try:
    with open(file_name) as file_object:
        words = file_object.read()
except FileNotFoundError:
    print(file_name + "文件不存在" )
else:
    print(words)




