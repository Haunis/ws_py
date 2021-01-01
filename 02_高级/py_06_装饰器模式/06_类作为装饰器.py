"""
使用类作为修饰器

"""


class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("__call__ 被调用")  # 可以用作权限验证
        return self.func()

    @staticmethod
    def say_hello(func):
        print("say_hello,func=", func)
        return func


print("----------1.@Test-------------")


@Test  # 相当于 foo = Test(foo) #Test的__init__（）会被调用
def foo():
    return "hello"


print(foo())  # 对象名加括号，会回调__call__()方法

print("----------2.@Test.say_hello-------------")


@Test.say_hello  # 相当于 foo = Test.say_hello(foo)
def foo():
    return "hello"


print("foo:", foo())
