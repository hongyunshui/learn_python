#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-14 21:12
@Author  : hys
@Site    : 
@File    : 作用域.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
ff = "kk"
if True:
    print(ff)
    ff = "flag"
    print(ff)

print(ff)

while True:
    print(ff)
    ff = "ll"
    break

print(ff)

ff = "kk"


def test():
    print(ff)
    ff = "ii"
