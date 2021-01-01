# -*-coding:utf-8-*-
"""
__dict__:查看类或者对象的所有属性

__init__:就是一个变量,指向一个方法
"""


class Demo:
    def __init__(self, name):
        self.__name = name


d = Demo("demo1")

# print(d.__dict__)
print(Demo.__dict__)
