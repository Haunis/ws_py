"""
装饰参数不定长的函数

本demo的装饰器也是通用装饰器
可以装饰无参函数和有参函数,装饰有参时可以装饰定长和不定长
也可以装饰无返回值和有返回值的函数
"""


def get_decorator(func):
    # *args表示用元组接受多个数值,**kwargs表示用字典接受多个键值对参数
    def decorator(*args, **kwargs):
        print("decorator called")
        return func(*args, **kwargs)  # *--对元组拆包,**--对字典拆包

    return decorator


@get_decorator  # 语法糖； 等价于 test = get_decorator(test)
def test(num, *args, **kwargs):
    print("test called,num=%d" % num)
    print("test called, ", args)
    print("test called, ", kwargs)
    return "ok"


test(1)
print()
test(1, 2, 3)
print()
ret = test(1, 2, 3, name="zhangsan")
print("ret=", ret)
