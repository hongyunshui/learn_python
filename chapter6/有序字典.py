#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-15 17:22
@Author  : hys
@Site    : 
@File    : 有序字典.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages["hys"] = "c"
favorite_languages["ll"] = "python"
favorite_languages["jj"] = "java"
favorite_languages["hys"] = "scala"
for name, language in favorite_languages.items():
    print("\n" + name)
    print(language)
print(favorite_languages)

