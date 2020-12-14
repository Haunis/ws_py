"""
把类当字典用

类实现了__getitem,__setitem__,__delitem__就可以把该类当做字典用
"""


class Demo:
    def __init__(self):
        self.dict = dict()

    def __getitem__(self, key):
        print("getitem called")
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value
        print("setitem called")

    def __delitem__(self, key):
        print("delitem called")
        del self.dict[key]


d = Demo()
d["name"] = "张三"  # 自动调用__setitem__()
value = d["name"]  # 自动调用__getitem__()
del d["name"]

# d["name"]  #因为已经调用了del ,再调用该方法会报错
