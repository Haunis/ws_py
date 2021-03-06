#! /usr/bin/python3
"""
单继承:只有一个父类
继承：子类拥有父类所有属性和方法
格式：class zi(Fu)
zi类是Fu的派生类，zi从Fu类派生

继承的传递性：子类拥有父类的所有属性和方法，同时也拥有父类的父类的所有属性和方法

"""


class Animal:
    @staticmethod
    def static_run():  # 静态方法
        print("animal static_run")

    @classmethod
    def class_run(cls):  # 类方法
        print("animal class_run  cls=", cls)

    def run(self):  # 实例方法
        print("animal run")


class Dog(Animal):
    def bark(self):
        print("dog bark")


class XiaoTianQuan(Dog):
    def fly(self):
        print("xiatianquan fly")


print("----------------Dog--------------------------")
dog = Dog()
dog.bark()  # 实例方法
dog.run()  # 父类方法
Dog.class_run()  # 父类类方法
Dog.static_run()  # 父类静态方法

print("\n----------------哮天犬--------------------------")
xiao_tian_quan = XiaoTianQuan()
xiao_tian_quan.fly()  # 自己的实例方法
xiao_tian_quan.bark()  # 拥有父类的属性和方法
xiao_tian_quan.run()  # 拥有父类的父类的属性和方法
