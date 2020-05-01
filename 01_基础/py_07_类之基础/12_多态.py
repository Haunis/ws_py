#! /usr/bin/python3
"""
继承的好处：代码复用

多态:不同的子类对象调用相同的父类方法,产生不同的执行结果
要实现多态，就必须让子类重写父类方法,以继承和重写父类方法为前提

"""


class Fu(object):
    def fun(self):
        print("Fu fun")


class Zi(Fu):
    def fun(self):
        print("Zi fun")


class Person(object):
    def play(self, zi):
        print("person play")
        zi.fun()


fu = Fu()
zi = Zi()

person = Person()

person.play(fu)
person.play(zi)
