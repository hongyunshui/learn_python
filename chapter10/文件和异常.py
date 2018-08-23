#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-15 17:46
@Author  : hys
@Site    : 
@File    : 文件和异常.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
test = []
"""使用read()读取整个文件"""
with open("test.txt") as file_object:
    test = file_object.read()
    print(test)
print("&&&&&&")
# print(test)

"""将列表中的文件一行一行写入文件"""
with open("read_and_write", "w") as file_object0:
    for line in test:
        file_object0.write(line)

"""一行一行读取文件并一行一行处理"""
with open("read_and_write") as file_object1:
    print("***")
    for line in file_object1:
        print(line)

"""按行读取文件并存储到一个列表中"""
with open("test.txt") as file_object2:
    lines = file_object2.readlines()
print(lines)

