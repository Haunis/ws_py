"""
元类： 可以创建类的类

使用type()可以创建类
type("Dog", (), {"name": "tom", "age": 3})
    第一个参数:类名
    第二个参数:父类
    第三个参数:类属性，类方法，实例方法
"""


class Animal(object):
    def fun(self):
        print("Animal run")


def instance_method(self):
    print("instance_method called")


@classmethod
def cls_method(cls):
    print("cls_method called")


@staticmethod
def static_method():
    print("static_method called")


print(">>>>>>>>>>>>>>>>>>>>>>1.创建类对象<<<<<<<<<<<<<<<<<<<<<<<")

Dog = type("Dog", (Animal,), {"name": "tom",
                              "age": 3,
                              "instance_method": instance_method,
                              "cls_method": cls_method,
                              "static_method": static_method
                              })
print(type(Dog))  # <class 'type'>
help(Dog)
dog = Dog()
print("Dog.name:", Dog.name)

dog.instance_method()
Dog.cls_method()
Dog.static_method()

print(">>>>>>>>>>>>>>>>>>>>>>2.元类是元类创建的<<<<<<<<<<<<<<<<<<<<<<<")
# 实例对象是类对象创建的
print("dog.__class__ : ", dog.__class__)  # <class '__main__.Dog'>
# 类对象是元类创建的
print("dog.__class__.__class__ : ", dog.__class__.__class__)  # <class 'type'>
# 元类是元类创建的
print("dog.__class__.__class__.__class__ : ", dog.__class__.__class__.__class__)  # <class 'type'>
