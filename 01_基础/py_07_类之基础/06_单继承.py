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
    def static_run(cls):
        print("static_run")

    @classmethod
    def class_run(cls):
        print("class_run")

    def run(self):  # 实例方法
        print("run")


class Dog(Animal):
    def bark(self):
        print("bark")
        super().static_run(Dog)
        super().class_run()

    def static_run(cls):
        print("dog static_run")
        super().static_run(cls)
        super().class_run()


class XiaoTianQuan(Dog):
    def fly(self):
        print("fly")


print("----------------Dog--------------------------")
dog = Dog()
# dog.run()
# dog.bark()

dog.static_run()
# dog.class_run()

print("\n----------------哮天犬--------------------------")
xiao_tian_quan = XiaoTianQuan()
xiao_tian_quan.fly()
xiao_tian_quan.bark()  # 拥有父类的属性和方法
xiao_tian_quan.run()  # 拥有父类的父类的属性和方法
