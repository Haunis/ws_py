"""
使用类名()创建对象时,python会自动执行以下操作
    1.创建对象: __new__为对象在内存分配空间,并返回对象的引用.
            python解释器获得引用后,将引用作为第一个参数传给__init__方法
            __new__是object的静态方法
    2.自动调用初始化方法 __init__:可在此方法中进行属性初始值设定

__del__()
    对象从内存中释放时会调用
    del 对象名 可以删除对象,将对象从内存中释放

__str__()
    直接打印对象名时调用;相当于java里的toString()方法

"""


class Car:
    def __init__(self, color):  # 创建对象时会自动调用__init()__
        self.color = color

    def __del__(self):  # 对象销毁时调用
        print("__del__ executed")

    def __str__(self):  # 必须返回一个字符串
        return "__str__ executed: %s" % self.color


# car是全局变量,系统执行完程序后该变量才会被回收
car = Car("red")
print("car.color=%s" % car.color)

print(car)
del car  # 删除对象时,对象会回调__del__方法
print("程序执行完成")
