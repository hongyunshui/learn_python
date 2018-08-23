#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-16 12:54
@Author  : hys
@Site    : 
@File    : 练习.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
# 动手试一试
# 10-3 访客 ：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。


class ColoUserInformation:
    """收集用户信息"""
    def __init__(self):
        self.name = ""

    def input_info(self):
        name = input("请输入你的名字： ")
        self.name = name
        with open("guest.txt", "a") as guest:
            name = name + "\t"
            guest.write(name)


colo_user_info = ColoUserInformation()
colo_user_info.input_info()
print("中国人")
# 10-4 访客名单 ：编写一个while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，
# 并将一条访问记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
while True:
    nam = input("请输入你的名字： ")
    if nam == "q":
        break
    print("你好，" + nam + "！")
    with open("guest_book.txt", "a") as file_object:
        nam = nam + "\n"
        file_object.write(nam)
# 10-5 关于编程的调查 ：编写一个while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到
# 一个存储所有原因的文件中。
while True:
    nam = input("请输入你的名字： ")
    if nam == "q":
        break
    words = input("请输入你喜欢编程的原因： ")
    if words == "q":
        break
    with open("why_user_love_program.txt", "a") as file_object:
        words = words + "\n"
        nam = nam + ": "
        file_object.write(nam)
        file_object.write(words)


# 动手试一试
# 10-6 加法运算 ：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。在这种情况下，当你尝试将
# 输入转换为整数时，将引发TypeError 异常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的
# 任何一个值不是数字时都捕获TypeError 异常，并打印一条友好的错误消息。对你编写的程序进行测试：先输入两个数字，再输
# 入一些文本而不是数字。
# 10-7 加法计算器 ：将你为完成练习10-6而编写的代码放在一个while 循环中，让用户犯错（输入的是文本而不是数字）后能够
# 继续输入数字。
# 10-8 猫和狗 ：创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的
# 名字。编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except 代码块中，以便在文件不
# 存在时捕获FileNotFound 错误，并打印一条友好的消息。将其中一个文件移到另一个地方，并确认except 代码块中的代码将正
# 确地执行。
# 10-9 沉默的猫和狗 ：修改你在练习10-8中编写的except 代码块，让程序在文件不存在时一言不发。
# 10-10 常见单词 ：访问项目Gutenberg（http://gutenberg.org/ ），并找一些你想分析的图书。下载这些作品的文本文件或
# 将浏览器中的原始文本复制到文本文件中。你可以使用方法count() 来确定特定的单词或短语在字符串中出现了多少次。例如，
# 下面的代码计算'row' 在一个字符串中出现了多少次：
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2 >>> line.lower().count('row')
# 3
# 请注意，通过使用lower() 将字符串转换为小写，可捕捉要查找的单词出现的所有次数，而不管其大小写格式如何。
# 编写一个程序，它读取你在项目Gutenberg中获取的文件，并计算单词'the' 在每个文件中分别出现了多少次。


