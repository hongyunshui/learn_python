#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-15 9:56
@Author  : hys
@Site    : 
@File    : test_import.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
import test_import1  # 在同一个项目根目录下的模块可以直接导入
# from test_import1 import test_import, test_import_a
# from test_import1 import *
test_import1.test_import()
test_import1.test_import_a()
