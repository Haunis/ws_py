"""
“元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。
那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。” —— Python界的领袖 Tim Peters

本demo演示的是一个使用场景：
    已经定义好的一个类，需要将其类属性名，实例方法名，类属性方法名，静态属性方法名都改为大写

"""


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
class Foo(object, metaclass=upper_attr):
    bar = 'bip'


print(hasattr(Foo, 'bar'))  # False
print(hasattr(Foo, 'BAR'))  # True

f = Foo()
print(f.BAR)
