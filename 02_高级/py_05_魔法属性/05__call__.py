"""

实例对象加()会回调__call__, 如instance()
"""


class Demo:
    # def __call__(self, *args, **kwargs):
    def __call__(self, x):  # 该方式定义也行
        print("__call__ executed")


d = Demo()
d(1)
