"""
所谓魔法属性就是 调用python中的某个属性或者方法,python解释器会调用某个特殊的方法
如 d = Demo()会调用__init()__,print(d)会调用__str__

del 对象： 先回调__del__,再删除对象
实例对象加()会回调__call__, 如instance()
取对象的描述时会调用__str__方法
"""


class Demo:
    # def __call__(self, *args, **kwargs):
    def __call__(self, x):  # 该方式定义也行
        print("__call__ executed")

    def __del__(self):
        print("__del__ called")

    def __str__(self):
        return "this is Demo"


d = Demo()

print("--------------1.d()-----------------")
d(1)

print("\n--------------2.__str__()-----------------")
print(d)

print("\n--------------3.del d-----------------")
del d
