#! /usr/bin/python3
"""
继承的好处：代码复用

多态:不同的子类对象调用相同的父类方法,产生不同的执行结果
要实现多态，就必须让子类重写父类方法,以继承和重写父类方法为前提

跟c++和java不一样，在c++和java里是父类指向字类对象是多态

"""


class Fu(object):
    def fun(self):
        print("Fu fun")


class Zi(Fu):
    def fun(self):
        print("Zi fun")


class Zi_2(Fu):
    pass


class Person(object):
    def play(self, zi):  # 传入实例的重写了父类方法就调用该实例方法，否则调用父类方法
        zi.fun()


fu = Fu()
zi = Zi()
zi_2 = Zi_2()

person = Person()

person.play(fu)
person.play(zi)
person.play(zi_2)
