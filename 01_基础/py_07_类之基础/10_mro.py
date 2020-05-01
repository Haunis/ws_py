#! /usr/bin/python3
"""
MRO: method resolution order 
__mro__是类的内置属性，主要用户多继承时判断方法、属性的调用路径

object是所有类的基类

"""


class Fu1:
    def fun(self):
        print("Fu1 fun executed")


class Fu2:
    def fun(self):
        print("Fu2 fun executed")


class Zi(Fu2, Fu1):
    pass


zi = Zi()
zi.fun()
print(Zi.__mro__)
