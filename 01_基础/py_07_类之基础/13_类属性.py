#! /usr/bin/python3

"""
类属性：就是java里静态变量
定义：在类的内部定义一个变量即可
访问：1.类名.属性  2.对象名.属性(不推荐)

每个对象都有__class__属性，该属性就是类对象

属性获取机制：
	向上查找机制：如果使用对象名访问某个属性，先从实例对象内部查找；
				没找到的话就再从类对象查找，再没找到就报错;

使用类属性时不建议使用"对象名.类属性"的方式.
使用"对象名.类属性"获取类属性的值是没问题的,但是这样给类属性赋值是不会成功的. 这样的赋值实际上是给实例对象的属性赋值,而不是给类属性赋值
"""


class Tool:
    count = 0  # 定义类属性

    def __init__(self, name):
        self.name = name
        Tool.count += 1  # 访问类属性，并为其赋值


tool1 = Tool("斧头")
tool2 = Tool("榔头")

print("tool1.count = %d" % tool1.count)

tool1.count = 100;  # 实际上是给实例对象的属性赋值,而不是给类属性赋值
print("Tool.count = %d" % Tool.count)  # 类属性的值还是2
print("tool1.count = %d" % tool1.count)  # 实例对象的属性 100

print("tool1.__class__:", tool1.__class__)  # 每个对象都有__class__属性，该属性就是类对象
print("tool1.__class__.count:", tool1.__class__.count)  # 2,就是类对象的类属性
