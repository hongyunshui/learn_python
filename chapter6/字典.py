#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-13 9:01
@Author  : hys
@Site    : 
@File    : 字典.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""
alien_0 = {"color": "green", "point": "5"}
print(alien_0["color"])
print(alien_0["point"])

# 6.2　使用字典
# 在Python中，字典是一系列键—值对 。每个键 都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、
# 字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。
print(alien_0)

# 6.2.1　访问字典中的值
# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键，如下所示：
print(alien_0["color"])

new_point = alien_0["point"]
print("你将获得" + str(new_point) + "个点数")

# 6.2.2  添加键—值对
# 字典是一种动态结构，可随时在其中添加键—值对。要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
# 下面在字典alien_0 中添加两项信息：外星人的 x 坐标和 y 坐标，让我们能够在屏幕的特定位置显示该外星人。我们将这个外星人放在屏
# 幕左边缘，且离屏幕上边缘25像素的地方。由于屏幕坐标系的原点通常为左上角，因此要将该外星人放在屏幕左边缘，可将 x 坐标设置为
# 0；要将该外星人放在离屏幕顶部25像素的地方，可将 y 坐标设置为25，如下所示：
alien_0["x_position"] = 0
alien_0["y_position"] = 9
print(alien_0["x_position"])
print(alien_0["y_position"])

# 6.2.3　先创建一个空字典
# 有时候，在空字典中添加键—值对是为了方便，而有时候必须这样做。为此，可先使用一对空的花括号定义一个字典，再分行添加各个
# 键—值对。例如，下例演示了如何以这种方式创建字典alien_0 ：
alien_1 = {}
print(alien_1)
alien_1["color"] = "red"
alien_1["point"] = 15
print(alien_1)

alien_1["color"] = "yellow"
print(alien_1["color"])

alien_0["speed"] = "fast"
print(alien_0["speed"])
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 3
elif alien_0["speed"] == "fast":
    x_increment = 5
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(alien_0["x_position"])

# 6.2.5删除键—值对
# 对于字典中不再需要的信息，可使用del 语句将相应的键—值对彻底删除。使用del 语句时，必须指定字典名和要删除的键。
print(alien_1)
del alien_1["point"]
print(alien_1)

# 6.2.6由类似对象组成的字典
# 在前面的示例中，字典存储的是一个对象（游戏中的一个外星人）的多种信息，但你也可以使用字典来存储众多对象的同一种信息。
favorite_languages = {
    "hys": "c",
    "lpp": "java",
    "zjh": "python",
    }
print(favorite_languages)

# 6.3遍历字典
# 一个Python字典可能只包含几个键—值对，也可能包含数百万个键—值对。鉴于字典可能包含大量的数据，Python支持对字典遍历。字典可用于以各种方式存储信息，因此有多种
# 遍历字典的方式：可遍历字典的所有键—值对、键或值。
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print("\nkey:" + key)
    print("value" + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, favorite_language in favorite_languages.items():
    print(name.title() + "'s favoritelanguage is " + favorite_language.title())
# 注意，即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。

# 6.3.3按顺序遍历字典中的所有键
# 字典总是明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。这不是问题，因为通常你想要的只是获取与键相
# 关联的正确的值。要以特定的顺序返回元素，一种办法是在for 循环中对返回的键进行排序。为此，可使用函数sorted() 来获得按特定顺序
# 排列的键列表的副本：
favorite_languages["pp"] = "c"
for name in sorted(favorite_languages.keys()):
    print(name.title())
print("***********")
for language in favorite_languages.values():
    print(language)
print("**************")
# 使用set去除value中重复的值
for language in set(favorite_languages.values()):
    print(language.title())

# 6.4嵌套
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套 。你可以在列表中嵌套字典、在字典中嵌套列表甚至
# 在字典中嵌套字典。正如下面的示例将演示的，嵌套是一项强大的功能。
alien_0 = {"color": "green", "point": "5"}
alien_1 = {"color": "yellow", "point": "10"}
alien_2 = {"color": "red", "point": "15"}
aliens = [alien_0, alien_1, alien_2]
print(aliens)
print(aliens[2])

for number in range(0,30):
    new_alien = {"color": "green", "point": "5", "speed": "slow"}
    aliens.append(new_alien)
print(aliens[:6])
cnt = 1
for alien in aliens[:5]:
    print(alien)
    print(cnt)
    cnt = cnt+1

# 修改前5个外星人
for alien in aliens[:5]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["point"] = "10"
print(aliens[:5])

# 6.4.2在字典中存储列表
# 有时候，需要将列表存储在字典中，而不是将字典存储在列表中。例如，你如何描述顾客点的比萨呢？如果使用列表，只能存储要添加的
# 比萨配料；但如果使用字典，就不仅可在其中包含配料列表，还可包含其他有关比萨的描述
favorite_languages = {
    "hys": ["c", "python"],
    "lpp": ["python", "java"],
    "jj": ["plc"],
}
for favorite_language in favorite_languages.items():
    print(favorite_language)

# 6.4.3在字典中存储字典
# 可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。例如，如果有多个网站用户，每个都有独特的用户名，可在字典中将用户名作
# 为键，然后将每位用户的信息存储在一个字典中，并将该字典作为与用户名相关联的值。在下面的程序中，对于每位用户，我们都存储了其
# 三项信息：名、姓和居住地；为访问这些信息，我们遍历所有的用户名，并访问与每个用户名相关联的信息字典：
hys = {"first_name": "zhao", "last_name": "jianhong", "addr": "zhengzhou"}
lpp = {"first_name": "li", "last_name": "panpan", "addr": "beijing"}
jj = {"first_name": "bei", "last_name": "jingjing", "addr": "shanghai"}
users = {"hys": hys, "lpp": lpp, "jj": jj}
for user_name, user_info in users.items():
    print("\nuser_name:", user_name)
    print("user_info:", user_info)


