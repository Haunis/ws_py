# -*-coding:utf-8-*-
"""
经典类和新式类都可以使用类属性的方式创建property属性

创建方式:类属性 = property(get,set,del,"doc")

Django就使用了类属性的方式创建了property属性
"""


class Person:
    def __init__(self):
        self.name = "temp name"

    def get_name(self):
        print("get_name called")
        return self.name

    def set_name(self, name):
        print("set_name called")
        self.name = name

    def del_name(self):
        print("del_name called")
        del self.name

    # 前三个参数传方法名,最后一个参数传字符串
    NAME = property(get_name, set_name, del_name, "temp doc...")


def main():
    p = Person()
    p.NAME  # 调用get_name()
    p.NAME = "张三"  # 调用set_name()
    doc = Person.NAME.__doc__  # 获取到property()最后一个参数
    print("doc:", doc)
    del p.NAME  # 调用del_name()


if __name__ == "__main__":
    main()
