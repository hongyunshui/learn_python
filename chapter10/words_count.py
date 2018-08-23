#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-16 22:53
# @Author  : hys
# @Site    : 
# @File    : words_count.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com


def word_count(file_name):
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        mes = file_name + "文件不存在"
        print(mes)
    else:
        words = contents.split()
        count = len(words)
        res = "此篇文章的单词数量是： " + str(count)
        print(res)


def word_count1(file_name):
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass  # 出现异常时什么都不做
    else:
        words = contents.split()
        count = len(words)
        res = "此篇文章的单词数量是： " + str(count)
        print(res)


file_name = "test_book"
word_count(file_name)

file_name = "words_count.txt"
word_count(file_name)



