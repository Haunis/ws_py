"""
如果定义好了函数,对函数添加功能可以用装饰器
如果定义好了类,对类进行添加功能可以用元类
"""


class UpperMetaClass(type):
    # class_name: str类型，类的名称
    # class_parents: 元组， 父类
    # class_attr: 字典，类属性，类方法，实例方法
    def __new__(cls, class_name, class_parents, class_attr):
        new_attr = {}
        for name, value in class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value

        # 调用type来创建一个类
        # return type(class_name, class_parents, new_attr)
        return type.__new__(cls, class_name, class_parents, new_attr)


def upper_attr(class_name, class_parents, class_attr):
    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    # 调用type来创建一个类
    return type(class_name, class_parents, new_attr)


# python解释器执行到这的时候，如果没有指定metaclass则使用默认的type()创建类
# upper_attr调用指定的方法，在方法里使用想要的type()创建类对象
# class Foo(object, metaclass=upper_attr):
class Foo(object, metaclass=UpperMetaClass):
    bar = 'bip'


print(hasattr(Foo, 'bar'))  # False
print(hasattr(Foo, 'BAR'))  # True

f = Foo()
print(f.BAR)  # bip
