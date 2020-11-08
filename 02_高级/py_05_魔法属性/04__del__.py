"""
del对象,先回调__del__,再删除对象

"""


class Demo:
    def __del__(self):
        print("__del__ called")


d = Demo()
del d
