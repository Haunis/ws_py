"""
实例对象加()会回调__call__, 如instance()
"""


class Demo:
    def __call__(self, *args, **kwargs):
        print("__call__ executed")


d = Demo()
d()
