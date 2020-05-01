"""
dir
    作用:查看对象所有的属性和方法
    说明:__fun__这样格式的方法是python提供的内置方法/属性,
        如 __new__ ,创建对象时自动调用
        __init__,对象初始化时自动调用
        __del__,对象销毁时自动调用
        __str__,返回对象的描述信息

"""


def fun(args):
    print(args)


print(dir(fun))  # 函数也是一个对象
