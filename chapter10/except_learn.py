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
try:
    print(str(5/0))
except ZeroDivisionError:
    print("除数不应该为0")
