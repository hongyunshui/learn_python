#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-16 22:28
# @Author  : hys
# @Site    : 
# @File    : division.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com
print("请输入两个数字： \n输入'q'退出")
while True:
    first_number = input("请输入第一个数字： ")
    if first_number == "q":
        break
    second_number = input("请输入第二个数字： ")
    if second_number == "q":
        break
    try:
        ans = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("除数不应该是0")
    else:
        print("两个数的商是： " + str(ans))

