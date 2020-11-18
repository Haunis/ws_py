"""
多个装饰器可以装饰同一个函数
按离函数的远近进行先后装饰,离函数近的先装饰
"""


def get_decorator1(func):
    print("get_decorator111")

    def decorator():
        print("decorator1 called 111")
        func()

    return decorator


def get_decorator2(func):
    print("get_decorator222")

    def decorator():
        print("decorator2 called 222 ")
        func()

    return decorator


# get_decorator1要装饰的是个函数,而@get_decorator2不是函数
# 所以@get_decorator2先装饰,@decorator1后装饰
@get_decorator1  # 语法糖； 等价于 test = get_decorator1(test)
@get_decorator2  # 语法糖； 等价于 test = get_decorator2(test)
def test():
    print("test called")


test()
"""
结果:
    get_decorator222        先调用get_decorator2装饰
    get_decorator111        再调用get_decorator1装饰
    decorator1 called 111
    decorator2 called 222 
test called

"""
