#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2018-03-14 9:56
@Author  : hys
@Site    : 
@File    : 函数.py
@Software: PyCharm
@Desc     :
@license : Copyright(C), Your Company
@Contact : george.zw513@gmail.com
"""

# 在本章中，你将学习编写函数 。函数是带名字的代码块，用于完成具体的工作。
# 要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，你无需反复编写完成该任务的代码，而只需调用执行该
# 任务的函数，让Python运行其中的代码。你将发现，通过使用函数，程序的编写、阅读、测试和修复都将更容易。
# 在本章中，你还会学习向函数传递信息的方式。你将学习如何编写主要任务是显示信息的函数，还有用于处理数据并返回一个或一组值的
# 函数。最后，你将学习如何将函数存储在被称为模块 的独立文件中，让主程序文件的组织更为有序。

# 8.1定义函数


def greet_user(usr_name):
    """显示简单问候语"""
    print("hello," + usr_name)


greet_user("hys")

# 8.2传递实参


def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type)
    print("my " + animal_type + "'s name is " + pet_name.title())


describe_pet("dog", "jingjing")
describe_pet("cat", "miao miao")

# 8.2.2关键字实参
describe_pet(pet_name='wang wang', animal_type='dog')
# 8.2.3默认值
# 编写函数时，可给每个形参指定默认值 。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。
# 因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。


def describe_pets(pet_name, animal_type="dog"):
    print("I have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name.title())


describe_pets("xiao huang")
describe_pets("miao miao2 ", "cat")

# 8.4传递列表
# 你经常会发现，向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）。将列表传递给函数后，函数就
# 能直接访问其内容。下面使用函数来提高处理列表的效率


def greet_users(names):
    """向列表中的每位用户都"发出简单的问候"""
    for name in names:
        print("hello " + name.title())


greet_users(["hys", "hong", "li pan pan"])

# 8.4.1在函数中修改列表
# 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。
up_printed_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []


def up_print_models(up_print_designs=[], complete_models=[]):
    """模拟打印每个设计，把打印好的移到另一个列表中"""
    while up_print_designs:
        current_design = up_print_designs.pop()
        print("Printing model: " + current_design)
        complete_models.append(current_design)


up_print_models(up_printed_designs[:], completed_models)
print("***")
print(up_printed_designs)
print(completed_models)
up_print_models()

# 8.4.2禁止函数修改列表
# 有时候，需要禁止函数修改列表。例如，假设像前一个示例那样，你有一个未打印的设计列表，并编写了一个将这些设计移到打印好的
# 模型列表中的函数。你可能会做出这样的决定：即便打印所有设计后，也要保留原来的未打印的设计列表，以供备案。但由于你将所有
# 的设计都移出了unprinted_designs ，这个列表变成了空的，原来的列表没有了。为解决这个问题，可向函数传递列表的副本而不是
# 原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。

# function_name(list_name[:])
# print_models(unprinted_designs[:], completed_models)

# 8.5传递任意数量的实参
# 有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。
# 例如，来看一个制作比萨的函数，它需要接受很多配料，但你无法预先确定顾客要多少种配料。下面的函数只有一个形参*toppings ，
# 但不管调用语句提供了多少实参，这个形参都将它们统统收入囊中：


def make_pizza(*topping):
    """打印所有传入的参数"""
    print(topping)


make_pizza("花生")
make_pizza("奶油", "牛肉", "水果")


# 8.5.1结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，
# 再将余下的实参都收集到最后一个形参中。
def make_fun(size, *topping):
    print(size)
    print(topping)  # topping 是一个元祖
    for top in topping:
        print(top)


make_fun(8, "dkjf")

# 8.5.2使用任意数量的关键字实参
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数
# 量的键—值对——调用语句提供了多少就接受多少。一个这样的示例是创建用户简介：你知道你将收到有关用户的信息，但不确定会
# 是什么样的信息。在下面的示例中，函数build_profile() 接受名和姓，同时还接受任意数量的关键字实参：


def build_profile(first, last, **profiles):  # profiles是一个字典
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    pfe = {"first_name": first, "last_name": last}
    for key, value in profiles.items():  # profiles是一个字典
        pfe[key] = value
    return pfe


profiles = build_profile("zhao", "jian hong", addr="zhengzhou", 职业="暂不找", age=28, sex="f")
print(profiles)
print("赵建宏")

# 8.6将函数存储在模块中
# 函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。你还可以更进一步，
# 将函数存储在被称为模块 的独立文件中，再将模块导入 到主程序中。import 语句允许在当前运行的程序文件中使用模块中的代码。
# 通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。
# 将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。

# 8.6.1导入整个模块
# 要让函数是可导入的，得先创建模块。模块 是扩展名为.py的文件，包含要导入到程序中的代码。下面来创建一个包含函数make_pizza()
# 的模块。为此，我们将文件pizza.py中除函数make_pizza() 之外的其他代码都删除：

# def make_pizza(size, *toppings):
# """概述要制作的比萨"""
# print("\nMaking a " + str(size) +
# "-inch pizza with the following toppings:")
# for topping in toppings:
# print("- " + topping)
# 接下来，我们在pizza.py所在的目录中创建另一个名为making_pizzas.py的文件，这个文件导入刚创建的模块，再调用make_pizza() 两次：
# making_pizzas.py
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# Python读取这个文件时，代码行import pizza 让Python打开文件pizza.py，并将其中的所有函数都复制到这个程序中。你看不到复制
# 的代码，因为这个程序运行时，Python在幕后复制这些代码。你只需知道，在making_pizzas.py中，可以使用pizza.py中定义的所有函数。
# 要调用被导入的模块中的函数，可指定导入的模块的名称pizza 和函数名make_pizza() ，并用句点分隔它们（见❶）。这些代码的输
# 出与没有导入模块的原始程序相同：
# Making a 16-inch pizza with the following toppings:
# - pepperoni
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese
# 这就是一种导入方法：只需编写一条import 语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。如果你使用这种i
# mport 语句导入了名为module_name.py的整个模块，就可使用下面的语法来使用其中任何一个函数：
# module_name.function_name()
# 8.6.2　导入特定的函数
# 你还可以导入模块中的特定函数，这种导入方法的语法如下：
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import function_0, function_1, function_2
# 对于前面的making_pizzas.py示例，如果只想导入要使用的函数，代码将类似于下面这样：
# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 若使用这种语法，调用函数时就无需使用句点。由于我们在import 语句中显式地导入了函数make_pizza() ，因此调用它时只需指定
# 其名称。
# 8.6.3　使用as 给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名 ——函数的另一个名称，
# 类似于外号。要给函数指定这种特殊外号，需要在导入它时这样做。
# 下面给函数make_pizza() 指定了别名mp() 。这是在import 语句中使用make_pizza as mp 实现的，关键字as 将函数重命名为你提
# 供的别名：
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# 上面的import 语句将函数make_pizza() 重命名为mp() ；在这个程序中，每当需要调用make_pizza() 时，都可简写成mp() ，而
# Python将运行make_pizza() 中的代码，这可避免与这个程序可能包含的函数make_pizza() 混淆。
# 指定别名的通用语法如下：
# from module_name import function_name as fn
# 8.6.4　使用as 给模块指定别名
# 你还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza 指定别名p ），让你能够更轻松地调用模块中的函数。相比
# 于pizza.make_pizza()
# ，p.make_pizza() 更为简洁：
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 上述import 语句给模块pizza 指定了别名p ，但该模块中所有函数的名称都没变。调用函数make_pizza() 时，可编写代码
# p.make_pizza() 而不是pizza.make_pizza() ，这样不仅能使代码更简洁，还可以让你不再关注模块名，而专注于描述性的函数名
# 。这些函数名明确地指出了函数的功能，对理解代码而言，它们比模块名更重要。
# 给模块指定别名的通用语法如下：
# import module_name as mn
# 8.6.5　导入模块中的所有函数
# 使用星号（* ）运算符可让Python导入模块中的所有函数：
# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# import 语句中的星号让Python将模块pizza 中的每个函数都复制到这个程序文件中。由于导入了每个函数，可通过名称来调用每个
# 函数，而无需使用句点表示法。然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法：如果模块中有函数的名称与
# 你的项目中使用的名称相同，可能导致意想不到的结果：Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别
# 导入所有的函数。最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。这能让代码更清晰，
# 更容易阅读和理解。这里之所以介绍这种导入方法，只是想让你在阅读别人编写的代码时，如果遇到类似于下面的import 语句，
# 能够理解它们：
# from module_name import *
# 8.7　函数编写指南
# 编写函数时，需要牢记几个细节。应给函数指定描述性名称，且只在其中使用小写字母和下划线。描述性名称可帮助你和别人明白代
# 码想要做什么。给模块命名时也应遵循上述约定。
# 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。文档良好的函数让其他程序员
# 只需阅读文档字符串中的描述就能够使用它：他们完全可以相信代码如描述的那样运行；只要知道函数的名称、需要的实参以及返回
# 值的类型，就能在自己的程序中使用它。
# 给形参指定默认值时，等号两边不要有空格：
# def function_name(parameter_0, parameter_1='default value')
# 对于函数调用中的关键字实参，也应遵循这种约定：
# function_name(value_0, parameter_1='value')
# PEP 8（https://www.python.org/dev/peps/pep-0008/ ）建议代码行的长度不要超过79字符，这样只要编辑器窗口适中，就能看到
# 整行代码。如果形参很多，导致函数定义的长度超过了79字符，可在函数定义中输入左括号后按回车键，并在下一行按两次Tab键，
# 从而将形参列表和只缩进一层的函数体区分开来。
# 大多数编辑器都会自动对齐后续参数列表行，使其缩进程度与你给第一个参数列表行指定的缩进程度相同：
# def function_name(
# parameter_0, parameter_1, parameter_2,
# parameter_3, parameter_4, parameter_5):
# function body...
# 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什
# 么地方开始。所有的import 语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。
