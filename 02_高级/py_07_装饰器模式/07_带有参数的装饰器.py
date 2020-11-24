"""
@set_level(1)
test1
相当于执行了两步:
    1. ret = set_level(1) #返回一个函数
    2. test1 = ret(test1) #使用该函数进行装饰

就是个语法糖
"""


def set_level(level):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level == 1:
                print("level 1 级别验证")
            elif level == 2:
                print("level 2 级别验证")
            func(*args, **kwargs)  # *args:对元组拆包

        return call_func  # 封装了func

    return set_func  # 用set_func进行装饰


@set_level(1)  # 调用set_level(1),用其返回的函数进行装饰
def test1():
    print("test1 called")
    return "test1"


@set_level(2)
def test2():
    print("test2 called")
    return "test2"


test1()
test2()
