#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-02-11 11:14
@Author  : hys
@Site    : 
@File    : list_brief_Introduction.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
# 列表 由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有
# 任何关系。鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters 、digits 或names ）是个不错的主意。

受邀人 = ['郝志国', '孟兆贵', '刘弦', '李海法']
for 师傅 in 受邀人:
    print(师傅 + "师傅" + "学生想请您到寒舍用餐，不知您明天中午是否有时间。")
print("小赵，我是" + 受邀人[1] + "很抱歉，我有事不能过去了。")
受邀人.remove("孟兆贵")
受邀人.insert(1, "周伟")
print("\n新受邀人名单：")
for 师傅 in 受邀人:
    print(师傅)

for 师傅 in 受邀人:
    print(师傅 + " 师傅学生想请您到寒舍用餐，不知您明天中午是否有时间。")


受邀人.insert(0, "赵英高")
受邀人.insert(2, "逢胜敏")
受邀人.append("钱军")
for 师傅 in 受邀人:
    print(师傅 + " 师傅学生想请您到寒舍用餐，不知您明天中午是否有时间。")

print("对不起，我只能邀请两位嘉宾。")

print(受邀人.__len__())

leng = 受邀人.__len__()

while leng > 2:
    师傅 = 受邀人.pop()
    print(师傅 + " 师傅，很是抱歉，我现在只能邀请两位来我这里吃饭，打算下次再宴请您。")
    leng = leng - 1

print("\n剩余名额：")
for 师傅 in 受邀人:
    print(师傅)

del 受邀人[1]
del 受邀人[0]
#验证是否完全删除
print("\tlast")
for 师傅 in 受邀人:
    print(师傅)


#组织列表
受邀人 = ['郝志国', '孟兆贵', '刘弦', '李海法']
受邀人.sort()

print(受邀人)

受邀人.sort(reverse=True)
print("\n反向排序：")
print(受邀人)

受邀人 = ['郝志国', '孟兆贵', '刘弦', '李海法']
print("\n列表未排序之前的顺序如下：")
print(受邀人)
print("\n 列表临时排序后的顺序如下：")
print(sorted(受邀人))
print("\n检查临时排序后是否恢复原来的顺序：")
print(受邀人)
#反转列表元素的排列顺序
受邀人.reverse()
print(受邀人)
#3.3.4　确定列表的长度
print(len(受邀人))






