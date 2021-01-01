"""
在原来函数内部代码不修改的情况下,增加新功能

格式:
@xxx_fun
def test():

@xxx_fun会调用xxx_fun函数进行装饰;
不是调用test()才开始装饰，写了@xxx_fun就会调用xxx__fun()进行装饰
"""


def get_decorator(func):
    def decorator():
        print("decorator called")
        func()

    return decorator


print("-------------1.@方式实现-------------")


@get_decorator  # 语法糖； 等价于 test = get_decorator(test);会调用get_decorator()
def test():
    print("test called")


test()

print("\n-------------2.手动调用闭包方式实现-------------")


def test():
    print("test called")


test = get_decorator(test)
test()
