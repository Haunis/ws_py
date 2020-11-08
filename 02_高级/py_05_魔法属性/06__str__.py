"""
获取对象的描述时会调用__str__方法
"""


class Demo:
    def __str__(self):
        return "this is Demo"


d = Demo()
print(d)
