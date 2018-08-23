#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-02-10 17:33
@Author  : hys
@Site    : 
@File    : variableAnd_DateType.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""

message = "Hello Python world!"
print(message)
#2.2.1变量的命名和使用
"""
在Python中使用变量时，需要遵守一些规则和指南。违反这些规则将引发错误，而指南旨在让你编写的代码更容易阅读和理解。请务必牢记下述有关变量的规则。
变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误。
不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print （请参见附录A.4）。
变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
要创建良好的变量名，需要经过一定的实践，在程序复杂而有趣时尤其如此。随着你编写的程序越来越多，并开始阅读别人编写的代码，将越来越善于创建有意义的变量名。
注意 　就目前而言，应使用小写的Python变量名。在变量名中使用大写字母虽然不会导致错误，但避免使用大写字母是个不错的主意。"""

#2.3.1　使用方法修改字符串的大小写
name = "ada lovelace"
print(name.title())

#2.3.2　合并（拼接）字符串

first_name = "ada"
last_name = "lovelace"
full_name = first_name+"      "+last_name
print(full_name)

print("hello,"+full_name.title()+"!")

#2.3.3　使用制表符或换行符来添加空白
print("python")
print("\tpython")
print("\n\nlanguages:\nPython\nJavaScript")

print("\n\nlanguages:\nPython\n\tJavaScript")



#2.3.4　删除空白

favorite_language = '    p    ython        '
print("favorite_language is "+favorite_language)
favorite_language = favorite_language.rstrip()
print("favorite_language is " + favorite_language)
print(favorite_language.lstrip())
print("    kaljfal    aljfa     ".strip())

message = "One of Python's strengths is its diverse community."
print(message)




#2.4.1　整数

print(2+3)
var = (2 + 3)*4
print(var)
var = 2 + 3 * 4
print(var)

var = 0.1 + 0.1
print(var)

var = 0.2 + 0.1
print(var)

print(3 * 0.1)

print(2+6)
print(2*4)
print(9-1)
print(str(16/2))