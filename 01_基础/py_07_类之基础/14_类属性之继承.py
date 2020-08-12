# -*-coding:utf-8-*-
"""
属性访问顺序:
    类外部属性(son.x) --> 当前类类属性(Son.x) -->父类类属性(Parent.x)
"""


class Parent(object):
    pass


class Son(Parent):
    pass


Parent.x = 100  # 添加类属性
print("Son.x:", Son.x, id(Son.x))  # 100, Son没有雷属性x,所以访问父类雷属性x
Son.x = 200  # 给Son类添加类属性
print("Son.x:", Son.x, id(Son.x))  # 200, Son类属性
print("Parent.x:", Parent.x, id(Parent.x))  # 100,父类的类属性不变还是100

print("---------son实例化---------")
son = Son()
print("son.x:", son.x)  # 200,优先访问Son类的类属性再访问父类类属性
son.x = 300  # 给类添加外部属性
print("son.x:", son.x)  # 300,外部属性
print("Son.x:", Son.x)  # 200,类属性还是200
