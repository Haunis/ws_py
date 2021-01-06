#! /usr/bin/python3
"""
MRO: method resolution order 
__mro__:
    是类的内置属性，主要用户多继承时判断方法、属性的调用路径
    是python解释器自己的c3算法决定的,c3算法保证每个继承链上的类只被调用一次

调用方法时,使用默认的类或者指定的类去mro里找该类的位置,找到后调用该类后面类的方法
    如Zi.__mro__ 是 (<class '__main__.Zi'>, <class '__main__.Fu1'>, <class '__main__.Fu2'>....
    Zi的后面是Fu1则调用Fu1里的方法

使用默认的类去mro里寻找:
    super().fun()--默认使用当前类
    zi.fun()--如果Zi没定义fun(),默认使用Zi去Zi的mro里寻找
使用指定类去mro寻找:
    super(Fu1,self).fun() --指定Fu1去调用处的类(Zi)的mro里寻找


类名.__mro__获取到的是个元组

object是所有类的基类

"""


class GrandPa(object):
    def __init__(self):
        print("====>>GrandPa init<<====")

    def fun(self):
        print("GrandPa fun executed")


class Fu1(GrandPa):
    def __init__(self):
        print("====>>Fu1 init<<====")
        super().__init__()

    def fun(self):
        print("Fu1 fun executed")


class Fu2(GrandPa):
    def __init__(self):
        print("====>>Fu2 init<<====")
        super().__init__()

    def fun(self):
        print("Fu2 fun executed")


class Zi(Fu1, Fu2):
    def __init__(self):
        print("====>>Zi init<<====")
        super().__init__()  # 默认使用当前类到mro里去寻找
        # super(Fu1, self).__init__()  # 使用Fu1到Zi的mro里去寻找;可以将Fu1替换其他类

        # Fu1.__init__(self)
        # Fu2.__init__(self) #这两个都调用的话会导致GrandPa 初始化两次

    # def fun(self):
    # super().fun() #默认使用当前类去mro寻找
    # super(Zi,self).fun() #默认使用当前类去mro寻找
    # super(Fu2, self).fun()  # 使用Fu2去mro里去寻找,调用mro里Fu2后面类的fun


zi = Zi()
zi.fun()  # 如果Zi没定义fun(),调用该方法时就会拿Zi到Zi的mro里去寻找Zi的位置,找到后调用其后面类的fun()
print(Zi.__mro__)

