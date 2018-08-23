#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-17 9:05
# @Author  : hys
# @Site    : 
# @File    : json存储数据.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com
import json
file_name = "number.json"
numbers = [1, 3, 5, 7, 9, 12]
t = ["sf", "sfs"]
with open(file_name, "w") as f_obj:
#    json.dump(numbers, f_obj)
    json.dump({"a": numbers, "b": t}, f_obj)

with open(file_name) as f_obj:
    num = json.load(f_obj)
    print(num)



